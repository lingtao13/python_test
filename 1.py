#!/usr/bin/python3
# _*_ coding:utf-8 _*_
from datetime import datetime

__author__ = 'nelson'
__date__ = '2018/4/19 下午1:28'



a='0|68444620|73334399.0|35000.0|35000.0|35000.0| 60 months| 11.99%|778.38|C|C1|Foreign Service Officer|10+ years|MORTGAGE|128000.0|Source Verified|Dec-2015|Issued|n|https://www.lendingclub.com/browse/loanDetail.action?loan_id=68444620||home_improvement|Home improvement|200xx|DC|6.46|0.0|Feb-1990|0.0|46.0||17.0|0.0|14277.0|27.4%|46.0|w|35000.0|35000.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0||0.0|Jan-2016|Jan-2016|0.0|56.0|1.0|INDIVIDUAL||||0.0|321.0|146867.0|1.0|11.0|0.0|0.0|28.0|35367.0|49.3|0.0|1.0|5020.0|40.1|52200.0|1.0|4.0|0.0'
print(a.split('|'))
b=a.split('|')
print(b)