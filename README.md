# Check-Error-And-Integration
此脚本用于分散文本的合并，并且可以对于gtavc.txt进行提供错误日志，免去手动查找无法生成gxt的原因
## 1（仅转换格式）格式工具.py
此工具会将文本批量转换为带分号的格式，例如：

<br>
[MAIN]<br>
ACCURA=Accuracy<br>
ADMIRAL=Admiral<br>
AMBULAN=Ambulance<br>
AMBUL_M='PARAMEDIC'<br>
<br>
将转换为<br>
  
<br>
[MAIN]<br>
;ACCURA=Accuracy<br>
ACCURA=Accuracy<br>
<br>
;ADMIRAL=Admiral<br>
ADMIRAL=Admiral<br>
<br>
;AMBULAN=Ambulance<br>
AMBULAN=Ambulance<br>
<br>
;AMBUL_M='PARAMEDIC'<br>
AMBUL_M='PARAMEDIC'<br>
<br>

***

## 2（仅整合+查错）格式工具.py
此工具会将文本整合成一个gtavc.txt的文本，并检查其中的错误语法，输出为CrashDump.txt的错误日志
