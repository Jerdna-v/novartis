from random import random, randint

import tornado.ioloop
import tornado.web
import tornado.httpserver
import sqlite3

def _personal():
    dbPath = 'db/recruits.db'
    connection = sqlite3.connect(dbPath)
    cursorobj = connection.cursor()
    try:
        cursorobj.execute("SELECT ID FROM basic ORDER BY id DESC LIMIT 1")
        id = cursorobj.fetchone()[0]+1
        sql_cmd = f'''CREATE TABLE IF NOT EXISTS experience{id} (
                    "job"	TEXT NOT NULL,
                    "years"	TEXT NOT NULL
                    );'''

        _execute(sql_cmd)

        sql_cmd2 = f'''CREATE TABLE IF NOT EXISTS education{id} (
                    "degree"	TEXT NOT NULL,
                    "field"	TEXT NOT NULL
                    );'''
        _execute(sql_cmd2)
        connection.commit()
    except Exception:
        raise
    connection.close()
    return id

def _execute(query):
    dbPath = 'db/recruits.db'
    connection = sqlite3.connect(dbPath)
    cursorobj = connection.cursor()
    try:
        cursorobj.execute(query)
        result = cursorobj.fetchall()
        connection.commit()
    except Exception:
        raise
    connection.close()
    return result

class Main(tornado.web.RequestHandler):
    def get(self):
        self.write("Main")

class AddStudent(tornado.web.RequestHandler):
    def get(self):
        self.render('Form/index.html')

    def post(self):

        id=int(_personal())
        first_name = self.get_argument("name")
        last_name = self.get_argument("surname")
        date_of_birth = self.get_argument("date")
        country = self.get_argument("country")
        city = self.get_argument("city")
        query = ''' insert into basic (ID,first_name,last_name,date_of_birth,country,city) values (%d,'%s', '%s', '%s', '%s', '%s') ''' % (id,first_name, last_name, date_of_birth, country, city);
        _execute(query)
        degree = self.get_argument("degree")
        field = self.get_argument("field")
        query = f''' insert into education{id} (degree,field) values ('%s', '%s') ''' % (degree,field);
        _execute(query)
        job = self.get_argument("job")
        years = self.get_argument("yearsjob")
        query = f''' insert into experience{id} (job,years) values ('%s', '%s') ''' % (job,years);
        _execute(query)
        email = self.get_argument("email")
        phone = self.get_argument("phone")
        query = ''' insert into contact (ID,email,phone) values (%d,'%s', '%s') ''' % (id,email,phone);
        _execute(query)
        fast_learner = self.get_argument("fastlearner",None)
        motivated = self.get_argument("motivated",None)
        self_initiative = self.get_argument("selfinitiative",None)
        shift = self.get_argument("shiftexperience",None)
        l=[fast_learner,motivated,self_initiative,shift]
        for i in range(len(l)):
            if l[i] is None:
                l[i]="false"
        other_skills = self.get_argument('otherskills')

        query = ''' insert into skill (learner,motivated,self_initiative,shift_experience,other_skills) values ('%s', '%s', '%s', '%s', '%s') ''' % (l[0],l[1],l[2],l[3], other_skills);
        _execute(query)
        english = self.get_argument("english",None)
        slovenian = self.get_argument("slovenian",None)
        other = self.get_argument("other",None)
        l=[english,slovenian,other]
        for i in range(len(l)):
            if l[i] is None:
                l[i]="false"
        query = ''' insert into language (english,slovenian,other) values ('%s', '%s', '%s') ''' % (l[0],l[1],l[2]);
        _execute(query)
        self.render('Form/done.html')


class ShowStudents(tornado.web.RequestHandler):
    def get(self):
        query = ''' select * from basic'''
        rows = _execute(query)
        self._processresponse(rows)

    def _processresponse(self, rows):
        self.write("<b>Records</b> <br /><br />")
        for row in rows:
            self.write(str(row[0]) + "      " + str(row[1]) + "     " + str(row[2]) + "     " + str(row[3]) + "      " + str(row[4]) + " <br />")

application = tornado.web.Application([
    (r"/", Main),
    (r"/create", AddStudent),
    (r"/show", ShowStudents),
], debug=True)

if __name__ == "__main__":
    random = 8000
    application.listen(random)
    tornado.ioloop.IOLoop.instance().start()