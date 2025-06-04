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
        
        hostname = data["hostname"]

        try:
            cursor.execute("""SELECT 
                            h.id,
                            h.hostname,
                            h.ipv4,
                            h.arch,
                            h.processor,
                            h.so,
                            h.distribution,
                            h.mem_total,
                            h.mem_free,
                            h.up_time,
                            h.mac_address,
                            h.created_at,
                            h.updated_at,
                            hi.env,
                            hi.url,
                            hi.is_internal,
                            hi.midleware,
                            hi.app_language,
                            hi.app_system,
                            hi.location,
                            hi.notes
                        FROM hosts h
                        INNER JOIN hosts_aditional_infos hi ON h.hostname = hi.hostname
                        WHERE h.hostname = "%s"
                        ORDER BY h.id""", (hostname,))
            results = cursor.fetchall()
            payload = []
            
            for result in results:
                payload.append({"id": result[0]})
                payload.append({"hostname": result[1]})
                payload.append({"ipv4": result[2]})
                payload.append({"arch": result[3]})
                payload.append({"processor": result[4]})
                payload.append({"so": result[5]})
                payload.append({"distribution": result[6]})
                payload.append({"mem_total": result[7]})
                payload.append({"mem_free": result[8]})
                payload.append({"up_time": result[9]})
                payload.append({"mac_address": result[10]})
                payload.append({"created_at": result[11]})
                payload.append({"updated_at": result[12]})
                payload.append({"env": result[13]})
                payload.append({"url": result[14]})
                payload.append({"is_internal": result[15]})
                payload.append({"midleware": result[16]})
                payload.append({"app_language": result[17]})
                payload.append({"app_system": result[18]})
                payload.append({"location": result[19]})
                payload.append({"notes": result[20]})

            print(payload)

            return payload
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
