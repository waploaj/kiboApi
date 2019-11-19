from kibo.Config.kasa import kasaa

class Item:
    """Class contain all the method info of items in database"""

    def exists(self,item_id):
        """Check if a given item_id is item that exists on database"""
        cursor = None
        try:
            cursor = kasaa()
            cursor.execute('SELECT COUNT(*) AS item FROM ospos_items WHERE ospos_items.deleted = 0 AND ospos_items.item_id  = %s',(item_id))
            row = cursor.fetchone()
            if int(row["item"]) < 1:
                return False
            else:
                return True
        except Exception as e:
            print(e)
        finally:
            cursor.close()

    def exists_barcode(self,barcorde):
        """Check if a given barcode is existed item
        we input barcode as str not int for case like 000125 if its int 000 would be ignored
        """
        cursor = None
        barcorde = str(barcorde)
        try:
            #TODO: comeback and check if allowed dublicate barcode is True;
            cursor = kasaa()
            cursor.execute("SELECT COUNT(*) AS item FROM ospos_items WHERE ospos_items.deleted = 0 AND ospos_items.item_number = %s",barcorde)
            row = cursor.fetchall()
            if row[0]["item"] < 1:
                return False
            else:
                return True
        except Exception as e:
            print(e)
        finally:
            cursor.close()



pip  = Item()
print(pip.exists_barcode(12345))