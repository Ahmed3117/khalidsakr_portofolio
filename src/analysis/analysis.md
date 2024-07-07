## accounts (app) (verbose_name=' الحسابات')

### Account (model) => can create only one object of it (verbose_name='البيانات الشخصية')
- name (verbose_name='الاسم')
- description
- caption
- image
- mail
- address
### Phone (model)
account (fk to Account)
phone_number
### SocialAccount (model)
- site
- url
- is_active

## centersplaces (app) (verbose_name=' اماكن التواجد')

### Government (model) (verbose_name=' المحافظة') 
- name
### Center (model) (verbose_name=' السنتر') 
- government (fk to Government)
- location 
- status
### Class (model)
- name
- status
### Dates (model) 
- center (fk to Center)
- status
- class (fk to Class)
- scadual (datetime)

## booksplaces (app) (verbose_name=' اماكن الكتب والمذكرات')

### Library (model) (verbose_name=' المكتبة') 
- name
- government (fk to Government)
- location 
- status
### Book (model)
- name
- description
- class (fk to Class)
- library (fk to Library)
- status

## news (app) (verbose_name='  اخر الاخبار ')

### Notification (model) (verbose_name=' الاشعار') 
- title
- description
- date_added (auto_now)
- date_start 
- date_end 
- priority (choices from(argent,normal) , default='normal')
- status
