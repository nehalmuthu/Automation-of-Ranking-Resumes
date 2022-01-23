import requests
from bs4 import BeautifulSoup

    
#main resume page
html_doc=requests.get("https://www.indeed.com/career-advice/resume-samples")
soup = BeautifulSoup(html_doc.text, 'html.parser')
m = soup.findAll("a", {"class": "styles-module--segment--aOzNJ"})
link=[]
for i in m:
    link.append('https://www.indeed.com'+i.get('href'))
#got all main profession name links
#l is the list of links containing profession names

link=link[0:2]

prof=[]
for l in link:
    html_doc=requests.get(l)
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    m = soup.findAll("a", {"class": "styles-module--segment--aOzNJ"})    
    l2=[]
    for i in m:
        l2.append('https://www.indeed.com'+i.get('href'))
        #under each profession we have a list of jobs
        #retrievd those links in l2
        
        #finally scrapping the the job resume
    job=[]
    for j in l2:
        html_doc=requests.get(j)
        soup = BeautifulSoup(html_doc.text, 'html.parser')
        m = soup.findAll("div", {"class": "styles-module--resumeContent--2TOaO"})
        m=m[0]
        w=[]
        t=m.findAll('p')
        for i in t:
            w.append(i.text)
            
        t=m.findAll('li')
        for i in t:
            w.append(i.text)
        job.append(w)
    prof.append(job)


#structure analysis
#<a href="/career-advice/resume-samples/administrative-resumes/administrative-assistant" class="styles-module--segment--aOzNJ">Administrative Assistant<svg xmlns="http://www.w3.org/2000/svg" focusable="false" role="img" fill="currentColor" viewBox="0 0 24 24" type="arrow-forward" aria-hidden="true" class="css-tcesgz e18c60hj0"><path d="M12.447 16.639a.5.5 0 010-.707l2.927-2.927H5.5a.5.5 0 01-.5-.5v-1a.5.5 0 01.5-.5h9.88l-2.937-2.937a.5.5 0 010-.707l.707-.707a.5.5 0 01.707 0l3.933 3.933.001-.001 1.061 1.06a.5.5 0 010 .708l-4.992 4.992a.5.5 0 01-.707 0l-.707-.707z"></path></svg></a>
#<a href="/career-advice/resume-samples/administrative-resumes" class="styles-module--segment--aOzNJ">Administrative Resumes<svg xmlns="http://www.w3.org/2000/svg" focusable="false" role="img" fill="currentColor" viewBox="0 0 24 24" type="arrow-forward" aria-hidden="true" class="css-tcesgz e18c60hj0"><path d="M12.447 16.639a.5.5 0 010-.707l2.927-2.927H5.5a.5.5 0 01-.5-.5v-1a.5.5 0 01.5-.5h9.88l-2.937-2.937a.5.5 0 010-.707l.707-.707a.5.5 0 01.707 0l3.933 3.933.001-.001 1.061 1.06a.5.5 0 010 .708l-4.992 4.992a.5.5 0 01-.707 0l-.707-.707z"></path></svg></a>




#html_doc=requests.get("https://www.linkedin.com/jobs/")
#soup = BeautifulSoup(html_doc.text, 'html.parser')
#s=soup.findAll("a")
#l=[]
#for i in s:
#    l.append(i.get('href'))


#for j in l2:
 #       html_doc=requests.get(j)
   #     soup = BeautifulSoup(html_doc.text, 'html.parser')
  #      m = soup.findAll("div", {"class": "styles-module--resumeContent--2TOaO"})
    #    m=m[0]
     #   w=[]
      # for i in t:
        #    w.append(i.text)
            
       # t=m.findAll('li')
       # for i in t:
       #     w.append(i.text)
       # job.append(w)
    #prof.append(job)

