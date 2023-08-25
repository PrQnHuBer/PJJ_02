#input คือการรับค่าทางแป้นพิมพ์
import setuptools


std_id =input('ป้อนชื่อ :')
std_name= input('ป้อนรหัสนักศึกษา : ')
std_year =input('ป้อนปีเกิด : ')
#ทุกสิ่งที่ป้อนเป็นString
#ตัวแปร Variable คือ ชื่อที่ตั้งขึ้นเองเป็นไปตามกฎ มีหน้าที่เก็บข้อมูลที่เกิดขึ้นในโปรแกรม
std_age =2023-int(std_year)
print(f'ยินดีต้อนรับ {std_id} รหัสนักศึกษา {std_name} ปีเกิด {std_year} อายุ {std_age}')
print('ยินดีต้อนรับ',std_id,'รหัสนักศึกษา',std_name,'ปีเกิด',std_year,'อายุ',std_age)
print('ยินดีต้อนรับ '+ str(std_id)+' รหัสนักศึกษา '+ str(std_name)+' ปีเกิด '+ str(std_year)+' อายุ '+str(std_age) )
print("ยินดีต้อนรับ {0} รหัสนักศึกษา {1} ปีเกิด {2} อายุ {3}".format( std_id, std_name, std_year,std_age))
print('ยินดีต้อนรับ %s รหัสนักศึกษา %s ปีเกิด %s อายุ %s '%(std_id,std_name,std_year,std_age))    