from kibo.Config.kasa import kasaa
from kibo.Config.database import bcrypt
import os,jsonify
from flask_login import UserMixin
class Employee(UserMixin):
    """Contain all attribute and methods of calling an employee"""

    def exists(self,person_id):
        """Check if given person__id is an employee and exists"""
        try:
            cursor = kasaa()
            row = cursor.execute("SELECT * FROM ospos_employees WHERE ospos_employees.person_id = %s",(person_id))
            if  row > 0:
                return True
            else:
                return False
        except Exception as e:
            #TODO: comeback and handle smtp mail for error notification
            print(e)
        finally:
            cursor.close()

    def get_total_row(self):
        """Return the total number of employees in database"""
        cursor = None
        try:
            cursor = kasaa()
            row = cursor.execute("SELECT * FROM ospos_employees WHERE ospos_employees.deleted = 0")
            return row
        except Exception as e:
            print(e)
        finally:
            cursor.close()

    def get_all(self,limit=10000,offset=0):
        """Get all Employee from database"""
        cursor = None
        try:
            cursor = kasaa()
            cursor.execute(
                "SELECT * FROM ospos_employees INNER JOIN ospos_people ON ospos_people.person_id = ospos_employees.person_id WHERE ospos_employees.deleted =0 ORDER BY ospos_people.first_name ASC LIMIT %s OFFSET %s",(limit,offset)
            )
            row = cursor.fetchall()
            return row
        except Exception as e:
            print(e)
        finally:
            cursor.close()
    def get_info(self,employee_id):
        """Get a  particular  employee infomation from database"""
        try:
            cursor = kasaa()
            cursor.execute(
                "SELECT * FROM ospos_employees INNER JOIN ospos_people ON ospos_people.person_id = ospos_employees.person_id WHERE ospos_employees.deleted = 0 AND ospos_employees.person_id = %s ORDER BY ospos_people.first_name ASC" ,employee_id
            )
            row = cursor.fetchall()
            return row
        except Exception as e:
            print(e)
        finally:
            cursor.close()

    def get_multiple_info(self, employees_ids):
        """Get info of multiple Employees in database"""
        cursor = None
        try:
             for employee_id in employees_ids:
                 #TODO: comeback for multiple info of employee
                cursor = kasaa()
                cursor.execute(
                    "SELECT * FROM ospos_employees WHERE ospos_employees.deleted = 0 AND ospos_employees.person_id = %s ",
                    (employee_id)
                )
                row = cursor.fetchall()
                return row
        except Exception as e:
            print(e)
        finally:
            cursor.close()

    def save_employee(self,person_data,employee_data,grant_data):
        """Save the person data employee and permmision data in database"""
        cursor = None
        try:
            cursor = kasaa()
            if employee_data["person_id"] and Employee.exists(employee_data["person_id"]) == False:
                cursor = kasaa()
                cursor.execute("""
                INSERT INTO ospos_employees (username, password, person_id, deleted, hash_version, language, language_code)
                VALUES (%s, %s, %s, 0, 2, NULL, NULL);
                """,(employee_data["username"],employee_data["password"],employee_data["person_id"]))

            elif employee_data["person_id"] and Employee.exists(employee_data["person_id"]) == True:
                #TODO: comeback for upadate employee recodrs
                cursor.execute("""

                """)
        except Exception as e:
            print(e)
        finally:
            cursor.close()

    def login(self,username,password):
        """This methods Takes username and  password of an employee and attempts to login an"""
        cursor = None
        try:
            cursor = kasaa()
            cursor.execute("SELECT * FROM ospos_employees WHERE ospos_employees.username =  %s",(username))
            row = cursor.fetchone()
            if row != None:
                if bcrypt.check_password_hash(row["password"],password) == True:
                    return row
                else:
                    return ("Your Password is Incorrect")
            else:
                return ("User Not Found")
        except Exception as e:
            print(e)
        finally:
            cursor.close()

    def search_suggestion(self,search,limit=25):
        """This method takes the parameter search return the search suggestion of employees in database"""
        cursor = None
        suggestions = []
        try:
            cursor = kasaa()
            cursor.execute(
                '''
                SELECT ospos_people.first_name,ospos_people.last_name
                FROM ospos_employees
                INNER JOIN ospos_people ON ospos_employees.person_id = ospos_people.person_id
                WHERE ospos_employees.deleted = 0 AND ospos_people.first_name LIKE %s OR ospos_people.last_name LIKE %s 
                OR ospos_people.phone_number LIKE %s OR ospos_people.email LIKE %s
                ORDER BY ospos_people.first_name ASC LIMIT %s
                
                ''',(search,search,search,search,limit)
            )
            row  = cursor.fetchall()
            return row
        except Exception as e:
            print(e)
        finally:
            cursor.close()

pip = Employee()
print(pip.search_suggestion("abdallah@waploaj.com"))