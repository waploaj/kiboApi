from kibo.Config.kasa import kasaa

class Person:
    """This class contain the methods of all employee and customer(ie.person)"""

    def exists(self,person_id):
        """Check if the given person_id exists"""
        cursor = None
        try:
            cursor = kasaa()
            row = cursor.execute("SELECT * FROM ospos_people WHERE ospos_people.person_id = %s", (person_id))
            if row > 0:
                return True
            else:
                return False
        except Exception as e:
            # TODO: comeback and handle smtp mail for error notification
            print(e)
        finally:
            cursor.close()


