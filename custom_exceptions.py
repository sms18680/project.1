class InvalidAdminLoginError(Exception):

    def _str_(self):
        return "InvalidAdminLoginError : INCORRECT ADMIN NAME AND PASSWORD"
    
class InvalidUserLoginError(Exception):
    
    def _str_(self):
        return "InvalidUserLoginError : INCORRECT USER NAME AND PASSWORD"

class PreviousordersError(Exception):
    
    def _str_(self):
        return "No previous orders"