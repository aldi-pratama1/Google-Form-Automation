#!/usr/bin/env python
# coding: utf-8

# In[73]:


import pandas as pd
import requests


# In[74]:


#headers = ["no","email","nama","nama_kegiatan","jenis_kegiatan","tanggal_mulai","bulan_mulai","tahun_mulai","tanggal_selesai","bulan_selesai","tahun_selesai","durasi_pelaksanaan"]
df = pd.read_csv('https://github.com/aldi-pratama1/Google-Form-Automation/raw/main/Dataset/test%20form_3.csv', header = 0)
print(df.columns.values)



# In[75]:


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
    'referer': 'https://docs.google.com/forms/d/e/1FAIpQLSfhdWC3oJb7QeX6sLZb4o62PAv7ZqmcCvGzhMvrLi3heTFBhg/viewform?fbzx=-7744995320446650308',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'S=spreadsheet_forms=UT4sM9tFiB2_rTEiCazOJWN6-_JRfqichkxZSeNYGNI; SEARCH_SAMESITE=CgQI3pAB; CONSENT=YES+ID.id+202007; SID=2gd-keQ90uo2ujNmmqeYGeQpj6mtckVlMS8WWT0X3Awi6qkG7cAS5Kf2jX77zfPW3OGlZw.; __Secure-3PSID=2gd-keQ90uo2ujNmmqeYGeQpj6mtckVlMS8WWT0X3Awi6qkGyehj-hcZ03rkR8LzoBF-zQ.; HSID=ALBoZxketnhL1jFnh; SSID=ASYvUx0RD0TqCUEjI; APISID=h9hghE_JtzfHo-x2/AIHoYRc8SUWSvEGAD; SAPISID=e3oiXt5QZ6OmSta5/AEcjOTrWP-VnUEPSX; __Secure-3PAPISID=e3oiXt5QZ6OmSta5/AEcjOTrWP-VnUEPSX; ANID=AHWqTUmRm-VgnVo1i_zrQPlz1dVqTY2e7_dxlGuplyUfMGZSFnp4tzLSxdGAmuYb; NID=204=Q_LoU-qCTaIsUCijF7_ygZDwk5kmxgXVVP7W9I3HMWownfPbOR36t6hSwZ4fw7YhE-lIB-TSDsHe4Er_7PYQ-f8CNHnqnxnjZGn0LDCyjjcBCaUvrew7eLDEbvoCwyu1s_Wt0qR0LhPvtahnHOaT37srnG_4JzXvLHFwxhSIJj2pxO7EBw5yCuMeGs947Yuro3CGtnvG-V_s1-Xwn3APyTr9suJ9qwVPrLFnHNcvjLYBAg2T2OySWbZ4plkHKrxoY1Hwf5UQ9JFobomd0YAVsshiLfAbIr7DfPOEG7NZ9MRF0vyCjlD3I-ghpkjDMbyd; 1P_JAR=2020-10-24-05; SIDCC=AJi4QfHmgtdYS9jzAxHTIgFEpTCA6JErX2ILmCTyIJZtmZN6_e1r7Xq5s2y_XKrl-5p8KGXYlQ4; __Secure-3PSIDCC=AJi4QfF6GqQjIyy81hXp715G4GQ-BemoPyxrUCMUlzxx9TydneXv5FA4CDkVJaN8v3dKMzG_lU4',
    }

    data = {
      'entry.2026044433': str(nama[i]),
      'entry.1930627734': str(nama_kegiatan[i]),
      'entry.1937425491': str(durasi[i]),
      'entry.1899452181_year': str(tahun_mulai[i]),
      'entry.1899452181_month': str(bulan_mulai[i]),
      'entry.1899452181_day': str(tanggal_mulai[i]),
      'entry.1773655226_year': str(tahun_selesai[i]),
      'entry.1773655226_month': str(bulan_selesai[i]),
      'entry.1773655226_day': str(tanggal_selesai[i]),
      'entry.375568509': str(jenis_kegiatan[i]),
      'entry.999722910': 'Ya',
      'emailAddress': str(email[i]),
      'entry.375568509_sentinel': '',
      'entry.999722910_sentinel': '',
      'fvv': '1',
      'draftResponse': '[null,null,"-7744995320446650308"]\r\n',
      'pageHistory': '0',
      'fbzx': '-7744995320446650308'
    }

    response = requests.post('https://docs.google.com/forms/u/0/d/e/1FAIpQLSfhdWC3oJb7QeX6sLZb4o62PAv7ZqmcCvGzhMvrLi3heTFBhg/formResponse', headers=headers, data=data)

    i += 1
    
#sleep()
#wd.back()
#sleep())

