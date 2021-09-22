from WorkWithStringList import get_list_as_string, get_new_list_with, get_new_list_without_item, glue_two_string_lists


def get_sync_tables(headers_list, main_table_name = 'main_table', dublicate_table_name = 'dublicate_main_table'):
    
    # ['title', 'description', ...]
    headers_without_id = get_new_list_without_item(headers_list, 'id')
    print('headers_without_id: ', headers_without_id)
    
    # str: 'title', 'description', ...
    headers_without_id_str = get_list_as_string(headers_without_id)
    print('headers_without_id_str: ', headers_without_id_str)

    # ['r.title,', 'r.description,', ...]
    headers_with_spec_symbols = get_new_list_with(headers_without_id, 'r.', ', ')
    print('headers_with_spec_symbols: ', headers_with_spec_symbols)
    
    # str: r.title, r.description, ..., r.SOMEFIELD 
    headers_with_spec_symbols_str = get_list_as_string(headers_with_spec_symbols, '')
    print('headers_with_spec_symbols_str: ', headers_with_spec_symbols_str)

    # ['title = r.title,', 'description = r.description,', ...]
    glue_headers = glue_two_string_lists(headers_without_id, headers_with_spec_symbols)
    print('glue_headers: ', glue_headers)

    # title = r.title, description = r.description, ...
    glue_headers_str = get_list_as_string(glue_headers, '')
    print('glue_headers_str: ', glue_headers_str)

    return(
        f"""
        CREATE OR REPLACE FUNCTION count_rows_with_id(main_table_id integer) RETURNS SETOF bigint AS $$
    	BEGIN
                RETURN QUERY SELECT COUNT(*) FROM {dublicate_table_name} WHERE {main_table_name}_id = main_table_id;
            END;
        $$ LANGUAGE plpgsql;

        CREATE OR REPLACE FUNCTION equals_rows() RETURNS integer AS
            $BODY$
            DECLARE
                r {main_table_name}%rowtype;
                row_is_exist integer;
            BEGIN
                FOR r IN
                    SELECT * FROM {main_table_name} WHERE id > 0
                LOOP
                    row_is_exist := count_rows_with_id(r.id);
                    IF r.deleted_at IS NULL AND row_is_exist = 0 THEN 
                        --строка не найдена в {dublicate_table_name}
                        INSERT INTO {dublicate_table_name}(
                            {main_table_name}_id, 
                            {headers_without_id_str}
                        ) VALUES (          
                            r.id,           
                            {headers_with_spec_symbols_str}
                        );

                    END IF;

                    IF r.deleted_at IS NULL AND row_is_exist = 1 THEN 
                        --строка найдена в {dublicate_table_name}
                        UPDATE {dublicate_table_name} SET
                            {main_table_name}_id    = r.id, 
                            {glue_headers_str}  
                        WHERE
                            {main_table_name}_id 	= r.id;
                    END IF;
                END LOOP;
                RETURN row_is_exist;
        END;
        $BODY$
        LANGUAGE plpgsql;
        """,
        """
        SELECT * FROM equals_rows();
        """
    )