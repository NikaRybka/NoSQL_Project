class MESSAGES:
    INCORRECT_NAMESPACE_CODE = 202
    INCORRECT_TYPE_CODE = 207
    INCORRECT_GUARD_CODE = 205
    INCORRECT_KEY_CODE = 203
    USER_EXISTS_CODE = 201
    USER_NOT_EXISTS_CODE = 204
    TAG_NOT_EXISTS_CODE = 206
    ID_CHANGE_NOT_ALLOWED_CODE = 208
    FILE_NOT_EXISTS_CODE = 209
    NO_MATCH_CODE = 210

    OK_CODE = 100 #przyjmujemy dowolną wartość
    USER_ADDED_CODE = 101
    FILE_ADDED_CODE = 102
    USER_UPDATED_CODE = 103
    USER_DELETED_CODE = 104
    FILES_FOUND_CODE = 105
    TAG_DELETED_CODE = 106
    FILE_DELETED_CODE = 107
    FILE_UPDATED_CODE = 108
    FILE_EXISTS_CODE = 109

    INCORRECT_NAMESPACE = {"code": INCORRECT_NAMESPACE_CODE, "success": False, "description": "Incorrect (nonexisting) namespace"}
    INCORRECT_TYPE = {"code": INCORRECT_TYPE_CODE, "success": False, "description": "Incorrect type"}
    INCORRECT_GUARD = {"code": INCORRECT_GUARD_CODE,  "success": False,"description": "Incorrect guard"}
    INCORRECT_KEY = {"code": INCORRECT_KEY_CODE, "success": False, "description": "Incorrect key"}
    USER_EXISTS = {"code": USER_EXISTS_CODE, "success": False, "description": "User already exists"}
    USER_NOT_EXISTS = {"code": USER_NOT_EXISTS_CODE, "success": False, "description": "User does not exist"}
    TAG_NOT_EXISTS = {"code": TAG_NOT_EXISTS_CODE, "success": False, "description": "Tag does not exist"}
    ID_CHANGE_NOT_ALLOWED = {"code": ID_CHANGE_NOT_ALLOWED_CODE, "success": False, "description": "Cannot update ID!"}
    FILE_NOT_EXISTS = {"code": FILE_NOT_EXISTS_CODE, "success": False, "description": "File does not exist"}
    NO_MATCH = {"code": NO_MATCH_CODE, "success": False, "description": "Found no matching files to the list of tags"}

    OK = {"code": OK_CODE, "success": True, "description": "OK"}
    USER_ADDED = {"code": USER_ADDED_CODE, "success":True, "description": "User added successfully"}
    FILE_ADDED = {"code": FILE_ADDED_CODE, "success":True, "description": "File added successfully"}
    USER_UPDATED = {"code": USER_UPDATED_CODE, "success":True, "description": "User updated successfully"}
    USER_DELETED = {"code": USER_DELETED_CODE, "success":True, "description": "User deleted successfully"}
    FILES_FOUND = {"code": FILES_FOUND_CODE, "success":True, "description": "Files found successfully"}
    TAG_DELETED = {"code": TAG_DELETED_CODE, "success":True, "description": "Tag deleted successfully"}
    FILE_DELETED = {"code": FILE_DELETED_CODE, "success":True, "description": "File deleted successfully"}
    FILE_UPDATED = {"code": FILE_UPDATED_CODE, "success":True, "description": "File updated successfully"}
    FILE_EXISTS = {"code": FILE_EXISTS_CODE, "success":True, "description": "File exists"}
    @classmethod
    def ok(cls, value, guard):
        result = cls.OK.copy()
        result["value"] = value
        result["guard"] = guard
        return result