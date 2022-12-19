import pprint
import uuid
from magic_store.kv_idea.store import Store
from magic_store.db.database import Database

def test():
    store = Store()
    result = store.put("key1", "test text")
    result = store.put("key1", "test text 2", namespace="osiolek")
    result = store.put("key1", "nierozwazna czynnosc")

    x = store.get("key1", namespace="osiolek")
    print(x)
    result = store.delete("key1", namespace="osiolek", guard=x["guard"])
    result = store.put("key1","def", namespace="osiolek")
    # result = store.put("key1", "xxxxxxxxxxxxxxx", guard=x["guard"])

    print(result)
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(store._store)

    result = store.save()
    print(result)


def testLoad():
    store = Store()
    result = store.load()
    print(result)
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(store._store)

if __name__ == '__main__':

    database = Database()

    user = {
        "imie": "Nika",
        "nazwisko": "Rybinska",
        "login": "Nika_Rybka"
    }
    database.createUser(user, "id1")
    database.searchUser("id1")
    userUpdate = {
        "imie": "Weronika",
        "nazwisko": "Rybinska",
        "login": "Nika_rybka",
    }
    database.updateUser("id1", userUpdate)
    # database.deleteUser("id1")
    file1 = {
        "file": "Zajecia1.R",
        "path": "E:\\Metody eksploracji danych\\Zajecia1\\Zajecia1.R",
    }
    file2 = {
        "plik": "Zaj2.R",
        "path": "E:\\Metody eksploracji danych\\Zajecia2\\Zaj2.R",
    }
    file3 = {
        "plik": "Praca_domowa1.R",
        "path": "E:\\Metody eksploracji danych\\Pd1\\Praca_domowa1.R",
    }
    file4 = {
        "plik": "Kolokwium1.txt",
        "path": "E:\\Metody eksploracji danych\\Kolokwium1.txt",
    }

    database.createFile("id1", ["Med", "Zajecia1"], file1)
    database.createFile("id1", ["Med", "Zajecia2"], file2)
    database.createFile("id1", ["Med", "Praca_domowa"], file3)
    database.createFile("id1", ["kolokwium"], file4)
    database.createFile("asdasdasd", ["kolos"], file4)
    #database.deleteUser("id1")

    # database.searchFileByTags("id1", ["Med", "Zajecia1"], 2)
    # database.searchFileByTags("id1", ["Med", "asdasdasd"], 2)

    # database.deleteTag("id1", "Med")
    # database.deleteFileFromTag("id1", "Med", "Zajecia2")
    #database.deleteFileFromAllTags("id1", "Zaj2.R")
    #database.deleteFileFromAllTags("id1", "Zaj2.R")
