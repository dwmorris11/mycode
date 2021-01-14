count = 0
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as logs:
    for log in logs:
        if log.find("- - - - -] Authorization failed") > -1:
            count += 1
print(count)
