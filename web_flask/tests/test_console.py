        """
        # delete the database to avoid conflicting
        # names
        from models import storage as f_storage
        f_storage.empty()

        with patch('sys.stdout', new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Place name=15")
        clean_output = out_put.getvalue()

        self.assertRegex(clean_output, r"\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\n")
        # see if this created object is stored in the file.json
        with open("file.json", "r") as storage:
            db = storage.read()
            # check if the data is stored correclt in the file storage
            result = re.findall("Place."+clean_output[:-1], db)
            self.assertTrue(len(result) == 1)

            result = re.findall("\"name\": 15", db)
            self.assertTrue(len(result) == 1)

    def test_create_valueTypeWrong(self):
        """
        Test the create method with paramaetrs that have a string value
        """
        # delete the database to avoid conflicting
        # names
        from models import storage as f_storage
        f_storage.empty()

        with patch('sys.stdout', new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Place name=_15")
        clean_output = out_put.getvalue()

        self.assertRegex(clean_output, r"\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\n")
        # see if this created object is stored in the file.json
        with open("file.json", "r") as storage:
            db = storage.read()
            # check if the data is stored correclt in the file storage
            result = re.findall("Place."+clean_output[:-1], db)
            self.assertTrue(len(result) == 1)

            result = re.findall("\"name\": \"_15\"", db)
            self.assertTrue(len(result) == 0)


class TestShow(unittest.TestCase):
    """Test show"""
    pass
