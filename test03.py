#input คือการรับค่าทางแป้นพิมพ์
import setuptools


std_id =input('ป้อนชื่อ :')
std_name= input('ป้อนรหัสนักศึกษา : ')
std_year =input('ป้อนปีเกิด : ')
#ทุกสิ่งที่ป้อนเป็นString
#ตัวแปร Variable คือ ชื่อที่ตั้งขึ้นเองเป็นไปตามกฎ มีหน้าที่เก็บข้อมูลที่เกิดขึ้นในโปรแกรม
std_year =2023-int(std_year)
print(f'ยินดีต้อนรับ {std_id} รหัสนักศึกษา {std_name} อายุ {std_year}')
print('ยินดีต้อนรับ',std_id,'รหัสนักศึกษา',std_name,'อายุ',std_year)
print('ยินดีต้อนรับ '+ str(std_id)+' รหัสนักศึกษา '+ str(std_name)+' อายุ '+ str(std_year))
print("ยินดีต้อนรับ {0} รหัสนักศึกษา {1} อายุ {2}".format( std_id, std_name, std_year))
print('ยินดีต้อนรับ %s รหัสนักศึกษา %s อายุ %s'%(std_id,std_name,std_year))