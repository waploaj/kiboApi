from kibo.Config.kasa import kasaa


class Item:
    """Class contain all the method info of items in database"""

    def exists(self, item_id):
        """Check if a given item_id is item that exists on database"""
        cursor = None
        try:
            cursor = kasaa()
            cursor.execute('SELECT * item FROM ospos_items WHERE ospos_items.deleted = 0 AND ospos_items.item_id  = %s',
                           (item_id))
            row = cursor.rowcount
            if row < 1:
                return False
            else:
                return True
        except Exception as e:
            print(e)
        finally:
            cursor.close()

    def exists_barcode(self, barcorde):
        """Check if a given barcode is existed item
        we input barcode as str not int for case like 000125 if its int 000 would be ignored
        """
        cursor = None
        barcorde = str(barcorde)
        try:
            # TODO: comeback and check if allowed dublicate barcode is True;
            cursor = kasaa()
            cursor.execute("SELECT * FROM ospos_items WHERE ospos_items.deleted = 0 AND ospos_items.item_number = %s",
                           barcorde)
            row = cursor.rowcount
            if row < 1:
                return False
            else:
                return True
        except Exception as e:
            print(e)
        finally:
            cursor.close()

    def get_number_row(self):
        """Get all total nummber of row"""
        cursor = None
        try:
            cursor = kasaa()
            cursor.execute("SELECT * FROM ospos_items WHERE 1")
            row = cursor.rowcount
            return row

        except Exception as e:
            pass
        finally:
            cursor.close()

    def get_item_tax(self,item_id):
        """Get information about perticular Item"""
        cursor = None
        try:
            cursor = kasaa()
            cursor.execute("SELECT * FROM ospos_items_taxes WHERE ospos_items.item_id = %s",(item_id))
            row = cursor.fetchall()
            return row
        except Exception as e:
            pass
        finally:
            cursor.close()

    def get_infoby_item_id(self,item_id):
        """Get info of particular item"""
        cursor = None
        try:
            cursor = kasaa()
            cursor.execute("SELECT * FROM ospos_items WHERE ospos_items.item_id = %s",(item_id))
            row = cursor.fetchall()
            return row
        except Exception as e:
            pass
        finally:
            cursor.close()

    def get_multiple_info(self,items_ids=[]):
        """Get multiple info on items"""
        cursor = None
        try:
            cursor = kasaa()
            for item in items_ids:
                cursor.executemany("SELECT * FROM ospos_items WHERE ospos_items.item_id =%s",(items_ids))
                row = cursor.fetchall()
                yield row
        except Exception as e:
            pass
        finally:
            cursor.close()

    def get_itemby_itemNumber(self,barcode):
        """Get item id given item number or barcode"""
        cursor = None
        try:
            cursor = kasaa()
            cursor.execute("SELECT ospos_items.item_id FROM ospos_items WHERE ospos_items.deleted = 0 AND ospos_items.item_number = %s",(barcode))
            row = cursor.fetchall()
            if row:
                return row
            else:
                return "Item does not exist"
        except Exception as e:
            pass
        finally:
            cursor.close()

    def save_item(self,item_data):
        """Save the items data and updpate"""
        cursor = None
        try:
            item_id = item_data["item_id"]
            if Item.exists(item_id) == False:
                cursor = kasaa()
                cursor.execute("""
                INSERT INTO ospos_items (KEY,VALUE) VALUES {item_data}
                """)








pip = Item()
print(pip.get_itemby_itemNumber(125))
