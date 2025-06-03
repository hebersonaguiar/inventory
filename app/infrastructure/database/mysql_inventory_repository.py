from app.infrastructure.database.mysql_connection import get_mysql_connection

class MySQLInventoryRepository:
    # def get_inventory(self, data: dict) -> str:
    #     connection = get_mysql_connection()
    #     cursor = connection.cursor()

    #     try:
    #         cursor.execute("""
    #                 SELECT hostname 
    #                     FROM hosts h
    #                     WHERE h.hostname = "%s"
    #                 """, (
    #                     data["hostname"]
    #                 ))
    #         data = cursor.fetchall()
    #         hostname = []
    #         for result in data:
    #             hostname = {
    #                 result[0]
    #             }
    #         return hostname
    #     except Exception as e:
    #         connection.rollback()
    #         raise e
    #     finally:
    #         cursor.close()
    #         connection.close()

    def get_hostname(self, data: dict) -> str:
        connection = get_mysql_connection()
        cursor = connection.cursor()

        print("Insert: ", data["hostname"])
        hostname = data["hostname"]


        try:
            cursor.execute("SELECT hostname FROM hosts h WHERE h.hostname = %s", (hostname))
            data = cursor.fetchall()
            hostname = []
            for result in data:
                hostname = {
                    result[0]
                }
            return hostname
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            cursor.close()
            connection.close()

    def update_host(self, data: dict) -> None:
        connection = get_mysql_connection()
        cursor = connection.cursor()

        try:
            cursor.execute("""
                UPDATE hosts
                    SET ipv4 = '%s', 
                    arch = '%s', 
                    processor = '%s', 
                    so = '%s', 
                    distribution = '%s', 
                    mem_total = '%s', 
                    mem_free = '%s', 
                    up_time = '%s', 
                    mac_address = '%s',
                    updated_at = '%s' 
                    WHERE hostname = '%s'
                """,  (
                    data["ipv4"],
                    data["arch"],
                    data["processor"],
                    data["so"],
                    data["distribution"],
                    data["mem_total"],
                    data["mem_free"],
                    data["up_time"],
                    data["mac_address"],
                    data["updated_at"],
                    data["hostname"]
                ))
            connection.commit()
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            cursor.close()
            connection.close()


    def insert_host(self, data: dict) -> None:
        connection = get_mysql_connection()
        cursor = connection.cursor()

        try:
            cursor.execute("""
                INSERT INTO hosts (
                    hostname, 
                    ipv4, 
                    arch,
                    processor, 
                    so,
                    distribution, 
                    mem_total, 
                    mem_free,
                    up_time, 
                    mac_address,
                    created_at
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                data["hostname"],
                data["ipv4"],
                data["arch"],
                data["processor"],
                data["so"],
                data["distribution"],
                data["mem_total"],
                data["mem_free"],
                data["up_time"],
                data["mac_address"],
                data["created_at"]
            ))

            connection.commit()
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            cursor.close()
            connection.close()
