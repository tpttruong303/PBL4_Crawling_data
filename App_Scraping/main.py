import customtkinter as ctk
from exc_db import DB
from sending_email import EmailServer
from crawl_data import Spider
import schedule
import exc_schedule
import time
import threading

class App(ctk.CTk):

    def __init__(self):

        self.db_exc = DB()
        self.EServer = EmailServer()
        self.stop_run_continuously = exc_schedule.run_continuously_task()
        self.first_id_job = self.db_exc.get_recent_id()
        super().__init__()
        self.initialize_user_interface()
    
    def initialize_user_interface(self):
        
        self.geometry("700x400")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.title("App Scraping")

        self.lb_web_url = ctk.CTkLabel(self, 
                                       text='Url available', 
                                       text_color='white', 
                                       fg_color='transparent')
        
        self.cbb_web_url = ctk.CTkComboBox(self,
                                           values=['https://www.careerlink.vn/vieclam/list'],
                                           width=380)
        
        self.btn_crawl = ctk.CTkButton(self,
                                       text='Crawling',
                                       width=210,
                                       command=self.btn_crawling)
                
        self.lb_limit_page = ctk.CTkLabel(self, 
                                          text='Limit pages',
                                          text_color='white')
        
        self.btn_active_limit_page = ctk.CTkButton(self, 
                                                   text='>',
                                                   width=20,
                                                   command=self.btn_activating_limit_page)

        self.limit_page_input = ctk.CTkEntry(self)

        self.lb_limit_job_to_send = ctk.CTkLabel(self, 
                                          text='Limit jobs',
                                          text_color='white')
        
        self.btn_active_limit_job_to_send = ctk.CTkButton(self, 
                                                   text='>',
                                                   width=20,
                                                   command=self.btn_activating_limit_job)

        self.limit_job_to_send_input = ctk.CTkEntry(self,
                                                    width=130)

        self.lb_nums_new_job = ctk.CTkLabel(self,
                                            text='Nums new jobs',
                                            text_color='white')
        
        self.nums_new_job_input = ctk.CTkEntry(self,
                                               width=110)

        self.set_text(self.nums_new_job_input, '0')

        self.lb_schedule = ctk.CTkLabel(self,
                                        text='Schedule',
                                        text_color='white')
        
        self.btn_active_schedule = ctk.CTkButton(self, 
                                                 text='>',
                                                 width=20,
                                                 command=self.btn_activating_schedule)
        
        self.lb_sending_times = ctk.CTkLabel(self,
                                             text='Sending times',
                                             text_color='white')
        
        self.sending_times_input = ctk.CTkEntry(self,
                                               width=110)
        
        self.set_text(self.sending_times_input, '0')

        self.tab_tasks = ctk.CTkTabview(self,
                                        width=680,
                                        height=290)

        self.lb_web_url.place(x=10, y=10)
        self.cbb_web_url.place(x=90, y=10)

        self.lb_limit_page.place(x=10, y=40)
        self.btn_active_limit_page.place(x=90, y=40)
        
        self.lb_schedule.place(x=10,y=70)
        self.btn_active_schedule.place(x=90, y=70)
        
        self.lb_limit_job_to_send.place(x=260,y=40)
        self.btn_active_limit_job_to_send.place(x=320,y=40)

        self.lb_nums_new_job.place(x=480,y=40)
        self.nums_new_job_input.place(x=580,y=40)

        self.lb_sending_times.place(x=480,y=70)
        self.sending_times_input.place(x=580,y=70)

        self.btn_crawl.place(x=480, y=10)

        self.tab_tasks.place(x=10,y=100)

    def initalize_tab_interface(self, tab_task, schedule_text):
        lb_start = ctk.CTkLabel(tab_task,
                                text='Start time')

        start_input = ctk.CTkEntry(tab_task,
                                   width=130)

        self.set_text(start_input, exc_schedule.get_time())

        lb_times = ctk.CTkLabel(tab_task,
                                text='Times')
        
        times_input = ctk.CTkEntry(tab_task,
                                   width=30)

        self.set_text(times_input, '0')

        lb_schedule = ctk.CTkLabel(tab_task,
                                   text='Schedule')
        
        schedule_input = ctk.CTkEntry(tab_task,
                                      width=220)

        self.set_text(schedule_input, schedule_text)

        done_task_button = ctk.CTkButton(tab_task,
                                         text='Done task',
                                         width=70,
                                         command=self.btn_canceling_job)
        
        txt_box = ctk.CTkTextbox(tab_task,
                                 height=200,
                                 width=650)
        
        lb_start.place(x=10,y=0)
        start_input.place(x=75,y=0)
        lb_times.place(x=215,y=0)
        times_input.place(x=260,y=0)
        lb_schedule.place(x=300,y=0)
        schedule_input.place(x=360,y=0)
        done_task_button.place(x=585,y=0)
        txt_box.place(x=10,y=40)

    def initalize_schedule_interface(self):

        self.schedule_component = []

        self.lb_every = ctk.CTkLabel(self,
                                     text='Every')
        
        self.input_every = ctk.CTkEntry(self,
                                        width=30)
        
        self.set_text(self.input_every, '')
        
        self.cbb_every = ctk.CTkComboBox(self,
                                         values=['Seconds',
                                                 'Minutes',
                                                 'Hours',
                                                 'Days',
                                                 'Monday',
                                                 'Tuesday',
                                                 'Wednesday',
                                                 'Thursday',
                                                 'Friday',
                                                 'Saturday',
                                                 'Sunday'],
                                         width=120)
        
        self.lb_at_time = ctk.CTkLabel(self,
                                       text='At')
        
        self.input_at_time = ctk.CTkEntry(self)

        self.set_text(self.input_at_time, '')
        
        self.lb_every.place(x=90,y=70)
        self.input_every.place(x=130,y=70)
        self.cbb_every.place(x=160,y=70)
        self.lb_at_time.place(x=290,y=70)
        self.input_at_time.place(x=310,y=70)

        self.schedule_component.append(self.lb_every)
        self.schedule_component.append(self.input_every)
        self.schedule_component.append(self.cbb_every)
        self.schedule_component.append(self.lb_at_time)
        self.schedule_component.append(self.input_at_time)
    
    def clear_schedule_interface(self):
        for component in self.schedule_component:
            component.destroy()

    def check_condition_crawling(self, page_num, limit_page):
        if limit_page == '':
            return True
        else: 
            return page_num < int(limit_page)
                    
    def crawling(self, tab_show, limit_page, url):
        page_num = 0
        spider = Spider(url, self.db_exc)
        text_box_tab = tab_show.children['!ctktextbox']
        self.write_log(text_box_tab, 'Start crawling')
        while self.check_condition_crawling(page_num, limit_page):
            page_num += 1
            self.write_log(text_box_tab, f'Start crawling page {page_num}')
            job_links = spider.parse(f'{url}?page={page_num}')
            if len(job_links) == 0:
                self.write_log(text_box_tab,'There are no links to be crawled')
                break
            self.write_log(text_box_tab, f'{len(job_links)} links are ready to be crawled')
            new_job_links = []

            for link in job_links:
                if self.db_exc.check_dup_job(link) != True:
                    new_job_links.append(link)

            if len(job_links) - len(new_job_links) != 0:
                self.write_log(text_box_tab, f'{len(job_links) - len(new_job_links)} jobs are already in database')

            for link in new_job_links:
                time.sleep(0.5)
                new_thread = threading.Thread(target=spider.parse_job, args=(link, ))
                new_thread.start()

            old_nums_new_job = int(self.nums_new_job_input.get())
            new_nums_new_job = len(new_job_links)
            self.set_text(self.nums_new_job_input, old_nums_new_job + new_nums_new_job)
            self.write_log(text_box_tab, f'Page {page_num} is done')
        
        self.write_log(text_box_tab, 'Done crawling')

    def sending_email(self):
        nums_new_jobs = int(self.nums_new_job_input.get())
        self.set_text(self.nums_new_job_input, '0')
        if nums_new_jobs != 0:
            for email_receiver in self.db_exc.get_all_emails():
                ids = []
                desired_career = self.db_exc.get_desired_career(email_receiver)
                for id in range(self.first_id_job, self.first_id_job + nums_new_jobs):
                    raw_careers = self.db_exc.get_job_career(id)
                    careers = [career.strip() for career in raw_careers.split('/')]
                    for career in careers:
                        if career in desired_career:
                            ids.append(id)
                            break
                if len(ids) != 0:
                    self.EServer.send_email_jobs(email_receiver, ids)

        self.first_id_job = self.db_exc.get_recent_id()
        times = int(self.sending_times_input.get()) + 1
        self.set_text(self.sending_times_input, f'{times}')
    
    def check_condition_sending(self):
        if self.btn_active_limit_job_to_send.cget('text') == '>':
            limit_job = 30
        else:
            limit_job = int(self.limit_job_to_send_input.get())
        
        return int(self.nums_new_job_input.get()) > limit_job

    def write_log(self, text_box_tab, text):
        text_box_tab.insert(index='1.0', text=f'{text}\n')
        self.update_idletasks() 
 
    def set_text(self, component, text):
        component.delete(0, 'end')
        component.insert(0, text)

    def tasking(self, tab_show, limit_page, url):
        crawl_thread = threading.Thread(target=self.crawling, args=(tab_show, limit_page, url, ))
        crawl_thread.start()

        if self.check_condition_sending() == True:
            self.sending_email()
        
        times = int(tab_show.children['!ctkentry2'].get()) + 1
        self.set_text(tab_show.children['!ctkentry2'], f'{times}')

    def timing(self):

        if self.btn_active_schedule.cget('text') == '>':
            return 'One time'
        else:
            self.at_time = self.input_at_time.get()
            if self.at_time == '':
                self.at_time = exc_schedule.get_time().split(' ')[0]
            else:
                match exc_schedule.validate_time(self.at_time):
                    case '%H:%M:%S':
                        pass
                    case '%H:%M':
                        self.at_time = f'{self.at_time}:00'
                    case '%H':
                        self.at_time = f'{self.at_time}:00:00'
                    case False:
                        return 'One time'
                
            self.interval = self.input_every.get()
            if self.interval == '':
                self.interval = 1
            else:
                self.interval = int(self.interval)
            self.interval_attribute = self.cbb_every.get()
            sub_time = self.at_time.split(':')
            match self.interval_attribute:
                case 'Seconds':
                    self.at_time = ''
                    return f'Every {self.interval} {self.interval_attribute}'
                case 'Minutes':
                    self.at_time = f':{sub_time[-1]}'
                case 'Hours':
                    self.at_time = f'{sub_time[1]}:{sub_time[2]}'
                case 'Days':
                    pass
                case 'Monday':
                    pass
                case 'Tuesday':
                    pass
                case 'Wednesday':
                    pass
                case 'Thursday':
                    pass
                case 'Friday':
                    pass
                case 'Saturday':
                    pass
                case 'Sunday':
                    pass

            return f'Every {self.interval} {self.interval_attribute} at {self.at_time}'

    def scheduling(self, schedule_plan, tab_show, name_task, limit_page, url):
        if schedule_plan == 'One time':
            schedule.every().second.do(exc_schedule.set_one_time_job(self.tasking, tab_show, limit_page, url)).tag(f'{name_task}')
        else:
            match self.interval_attribute:
                case 'Seconds':
                    schedule.every(self.interval).seconds.do(self.tasking, tab_show, limit_page, url).tag(f'{name_task}')
                case 'Minutes':
                    schedule.every(self.interval).minutes.at(self.at_time).do(self.tasking, tab_show, limit_page, url).tag(f'{name_task}')
                case 'Hours':
                    schedule.every(self.interval).hours.at(self.at_time).do(self.tasking, tab_show, limit_page, url).tag(f'{name_task}')
                case 'Days':
                    schedule.every(self.interval).days.at(self.at_time).do(self.tasking, tab_show, limit_page, url).tag(f'{name_task}')
                case 'Monday':
                    schedule.every().monday.at(self.at_time).do(self.tasking, tab_show, limit_page, url).tag(f'{name_task}')
                case 'Tuesday':
                    schedule.every().tuesday.at(self.at_time).do(self.tasking, tab_show, limit_page, url).tag(f'{name_task}')
                case 'Wednesday':
                    schedule.every().wednesday.at(self.at_time).do(self.tasking, tab_show, limit_page, url).tag(f'{name_task}')
                case 'Thursday':
                    schedule.every().thursday.at(self.at_time).do(self.tasking, tab_show, limit_page, url).tag(f'{name_task}')
                case 'Friday':
                    schedule.every().friday.at(self.at_time).do(self.tasking, tab_show, limit_page, url).tag(f'{name_task}')
                case 'Saturday':
                    schedule.every().saturday.at(self.at_time).do(self.tasking, tab_show, limit_page, url).tag(f'{name_task}')
                case 'Sunday':
                    schedule.every().sunday.at(self.at_time).do(self.tasking, tab_show, limit_page, url).tag(f'{name_task}')

    def btn_crawling(self):
        limit_page = self.limit_page_input.get()
        url = self.cbb_web_url.get()
        name_page = self.cbb_web_url.get().split('.')[1]
        new_task_tab = self.tab_tasks.add(f'{name_page}')
        schedule_plan = self.timing()
        self.initalize_tab_interface(new_task_tab, schedule_plan)
        self.scheduling(schedule_plan, new_task_tab, name_page, limit_page, url)
        
    def btn_activating_limit_page(self):
        if self.btn_active_limit_page.cget('text') == '>':
            self.btn_active_limit_page.place(x=230, y=40)
            self.btn_active_limit_page.configure(text='<')
            self.limit_page_input.place(x=90, y=40)
        else:
            self.btn_active_limit_page.place(x=90, y=40)
            self.btn_active_limit_page.configure(text='>')
            self.limit_page_input.delete(0,'end')
            self.limit_page_input.place_forget()

    def btn_activating_schedule(self):
        if self.btn_active_schedule.cget('text') == '>':
            self.initalize_schedule_interface()
            self.btn_active_schedule.place(x=450,y=70)
            self.btn_active_schedule.configure(text='<')
        else:
            self.clear_schedule_interface()
            self.btn_active_schedule.place(x=90, y=70)
            self.btn_active_schedule.configure(text='>')

    def btn_activating_limit_job(self):
        if self.btn_active_limit_job_to_send.cget('text') == '>':
            self.btn_active_limit_job_to_send.place(x=450, y=40)
            self.btn_active_limit_job_to_send.configure(text='<')
            self.limit_job_to_send_input.place(x=320, y=40)
        else:
            self.btn_active_limit_job_to_send.place(x=320, y=40)
            self.btn_active_limit_job_to_send.configure(text='>')
            self.limit_job_to_send_input.delete(0,'end')
            self.limit_job_to_send_input.place_forget()

    def btn_canceling_job(self):
        job_name = self.tab_tasks.get()
        schedule.clear(job_name)
        self.tab_tasks.delete(job_name)

    def on_closing(self):
        self.db_exc.close_db()
        self.EServer.close_server()
        self.stop_run_continuously.set()
        super().destroy()

if __name__ == '__main__':
    app = App()
    app.protocol('WM_DELETE_WINDOW', app.on_closing)
    app.mainloop()