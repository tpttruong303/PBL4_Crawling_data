import mysql.connector

class DB:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Qh@61030803',
            database='job',
        )

        self.cur = self.conn.cursor()

    def check_dup_job(self, link):
        self.cur.execute("""select * from job.job_detail where link = %s""", (link,))
        result = self.cur.fetchone()
        if result is None:
            return False
        return True

    def get_recent_id(self):
        self.cur.execute("select id from job.job_detail")
        if self.cur.fetchone() is None:
            first_id = 1
        else:
            first_id = self.cur.fetchone()[0]

        self.cur.reset()

        self.cur.execute("select count(*) from job.job_detail")
        quantity = self.cur.fetchone()[0]

        return first_id + quantity

    def add_job(self, item, job_url):

        sql = """INSERT INTO job_detail (Title,Company,Image,Posting_date,Deadline,Salary,YOE,Type,Level,Education,Sex,Career,Age,ID_Job,Contact_with,Location,Note,Phone_number,Email,Language,Describe_job,Benefits,Skills,Link) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        self.cur.execute(sql, (
            item['Title'],
            item['Company'],
            item['Image'],
            item['Posting_date'],
            item['Deadline'],
            item['Salary'],
            item['YOE'],
            item['Type'],
            item['Level'],
            item['Education'],
            item['Sex'],
            item['Career'],
            item['Age'],
            item['ID_Job'],
            item['Contact_with'],
            item['Location'],
            item['Note'],
            item['Phone_number'],
            item['Email'],
            item['Language'],
            item['Describe_job'],
            item['Benefits'],
            item['Skills'],
            job_url
        ))
        self.cur.execute("COMMIT;")
        self.conn.commit()

    def get_all_emails(self):
        sql = """select email from job.users"""

        self.cur.execute(sql)

        result = self.cur.fetchall()

        emails = []
        for val in result:
            emails.append(val[0])

        return emails

    def get_desired_career(self, email):
        sql = """select desired_career from job.users where email = %s"""

        self.cur.execute(sql, (email,))

        career = self.cur.fetchone()[0]

        return career

    def get_job_career(self, id):
        sql = """select career from job.job_detail where id = %s"""

        self.cur.execute(sql, (id,))
        
        career = self.cur.fetchone()[0]

        return career
    
    def close_db(self):
        self.cur.close()
        self.conn.close()