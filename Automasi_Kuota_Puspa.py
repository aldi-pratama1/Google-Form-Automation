#!/usr/bin/env python
# coding: utf-8

# In[128]:


import pandas as pd
import requests


# In[129]:


#headers = ["no","email","nama","nama_kegiatan","jenis_kegiatan","tanggal_mulai","bulan_mulai","tahun_mulai","tanggal_selesai","bulan_selesai","tahun_selesai","durasi_pelaksanaan"]
df = pd.read_csv('https://raw.githubusercontent.com/aldi-pratama1/Google-Form-Automation/main/test%20form_3.csv?token=AQD4HB3IMBO2Z7PHAEVEU5C7SQGN4', header = 0)


# In[130]:


no = df.No.to_list()
email = df.Email_Address.to_list()
nama = df.Nama_Lengkap.to_list()
nama_kegiatan = df.Nama_Kegiatan.to_list()
jenis_kegiatan = df.Jenis_Kegiatan.to_list()
tanggal_mulai = df.tanggal_mulai.to_list()
bulan_mulai = df.bulan_mulai.to_list()
tahun_mulai = df.tahun_mulai.to_list()
tanggal_selesai = df.tanggal_selesai.to_list()
bulan_selesai = df.bulan_selesai.to_list()
tahun_selesai = df.tahun_selesai.to_list()
durasi = df.Durasi_Pelaksanaan.to_list()

start_record = 1

i = start_record-1
while i < no[i]:


    import requests

    headers = {
        'authority': 'docs.google.com',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'origin': 'https://docs.google.com',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'x-chrome-connected': 'source=Chrome,id=109861963159574214330,mode=0,enable_account_consistency=false,consistency_enabled_by_default=false',
        'x-client-data': 'CIq2yQEIpbbJAQjBtskBCKmdygEIlbjKAQisx8oBCPXHygEI58jKAQjpyMoBCLTLygEIic/KAQjb1coBCMLXygEYi8HKAQ==',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://docs.google.com/forms/d/e/1FAIpQLSeGsK5vt6YytuC-bB6ppg5kE15dShkOm-Li6RVPbUumRoncRA/viewform?fbzx=6663323972260911834',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'SEARCH_SAMESITE=CgQI3pAB; CONSENT=YES+ID.id+202007; SID=2gd-keQ90uo2ujNmmqeYGeQpj6mtckVlMS8WWT0X3Awi6qkG7cAS5Kf2jX77zfPW3OGlZw.; __Secure-3PSID=2gd-keQ90uo2ujNmmqeYGeQpj6mtckVlMS8WWT0X3Awi6qkGyehj-hcZ03rkR8LzoBF-zQ.; HSID=ALBoZxketnhL1jFnh; SSID=ASYvUx0RD0TqCUEjI; APISID=h9hghE_JtzfHo-x2/AIHoYRc8SUWSvEGAD; SAPISID=e3oiXt5QZ6OmSta5/AEcjOTrWP-VnUEPSX; __Secure-3PAPISID=e3oiXt5QZ6OmSta5/AEcjOTrWP-VnUEPSX; ANID=AHWqTUmRm-VgnVo1i_zrQPlz1dVqTY2e7_dxlGuplyUfMGZSFnp4tzLSxdGAmuYb; NID=204=IeeH9XrV7RkGxdTCsvsayEAKMTEqgUPUeozQjwc-vf5nd8QyAObUAxwfAL_x7TOAaqIxLmyH4y51M59j4T_4EmeligHuuSPX1Q27nfpY2-fv5BHryyuP5kxFWMbLWFMFaNKE9uTBXR18t3IHCDEJlyOmNPBl0jTcDB0A8nqFBcSLrtQYvD5ikDjSFjdrR_zeAWfJrU6LrIn64OjDrjPX5nkKjppfuRzGSVGEXyTtQ9NZZfVE3-xGY_BHqxDBE6RQgtSF0Lqi7HgMiJafhqkTF3bZn0oufk4z2F4-TRHy2rHq-f9OEzSYnNZYftimZVD-; 1P_JAR=2020-10-24-09; SIDCC=AJi4QfEsLRSeDnz17IWhajMI1JtJtU6uS-RfZcysftM1w_6m1MHrmBr-YAfM05A8VnIlQdTmaDo; __Secure-3PSIDCC=AJi4QfGig1rjV6BWYt_pm7Jk1-tDsGN5CSNJT6uKha4yZhfCEn3IqvXjTJKetU2moYpEIc9bNQE',
    }

    data = {
        'entry.306763205': str(nama[i]),
      'entry.656274251': str(nama_kegiatan[i]),
      'entry.309225544': str(durasi[i]),
      'entry.1717546377_year': str(tahun_mulai[i]),
      'entry.1717546377_month': str(bulan_mulai[i]),
      'entry.1717546377_day': str(tanggal_mulai[i]),
      'entry.416720105_year': str(tahun_selesai[i]),
      'entry.416720105_month': str(bulan_selesai[i]),
      'entry.416720105_day': str(tanggal_selesai[i]),
      'entry.1974997541': str(jenis_kegiatan[i]),
      'entry.595925460': 'Ya',
      'emailAddress': str(email[i]),
      'entry.1974997541_sentinel': '',
      'entry.595925460_sentinel': '',
      'emailReceipt': 'true',
      'g-recaptcha-response': '03AGdBq24v-_w7H_fKXqlgH1aGDms8Q-Yr4tVg6GHdLLmuX-tEGquC1SosmOb2lJL4IY-4bejjzOymlWTm5q8QP2E6ieXTnsKLnoY0C-mi549yMcgeTQLdMcQsxRvWqLWe5Hrx9iDPmhw2mXblEKCFjuWynNdXCWxPDuIwC0Se9uJ4UxNG2URlTGiI7GI_mwfCK3ys19pwpY1M2OXHtuuFeufzzeqpkhdO5CqXlCqkDzUawnXMN1E0lMS-6YwmO9vqD5Tn1R9FklEBEfKvp65VAgJ4p87hbP74cgO5jklYtZA6wJJySFUprVEGa1RZ4zHQXymUjxHttKSUqGmWP0e3mzgX_s_3NQ_NAuh7CvvCCejoJ6-Kv1kzWs1jfAaW7mdtbRf4GFoKKCZXm-vEsybzeOUrnemkvezySK0GnfSfpMCZy85-52kF_7gOt9fTfFrwP0ybuxqOYSHH',
      'fvv': '1',
      'draftResponse': '[null,null,"6663323972260911834"]\r\n',
      'pageHistory': '0',
      'fbzx': '6663323972260911834'
    }

    response = requests.post('https://docs.google.com/forms/u/0/d/e/1FAIpQLSeGsK5vt6YytuC-bB6ppg5kE15dShkOm-Li6RVPbUumRoncRA/formResponse', headers=headers, data=data)


    i += 1

#sleep()
#wd.back()
#sleep())
