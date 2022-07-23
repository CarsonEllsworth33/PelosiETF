import robin_stocks.robinhood as rs

class rh_bot():
    def __init__(self,poly_name) -> None:
        self.poly_tracker = poly_name

    def rh_login(self):
        #read login data from login.infosec
        with open("./secfiles/login.infosec","r") as f:
            rs.login(username=f.readline(),
                    password=f.readline(),
                    expiresIn=86400,
                    by_sms=True)



if __name__ == '__main__':
    money_printer = rh_bot("nancy pelosi")
    money_printer.rh_login()