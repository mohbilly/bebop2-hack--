import itertools

file = open("dic.txt","w")
a = ['cyse', 'cysE', 'cySe', 'cySE', 'cYse', 'cYsE', 'cYSe', 'cYSE', 'Cyse', 'CysE', 'CySe', 'CySE', 'CYse', 'CYsE', 'CYSe', 'CYSE']

b = ['@gmu', '@gmU', '@gMu', '@gMU', '@Gmu', '@GmU', '@GMu', '@GMU']
c = ["5933","1601","2008","2011","2013","4400","3252", "2014", "2016", "2012", "2019", "2017", "2015", "2010", "2007", "1995", "1320", "1703", "1998", "1981", "2000", "1842", "3100", "2006", "4444", "3100", "1569", "3512", "3521", "3032", "3040", "4136", "1994", "2003", "2419", "1575", "2007", "2006", "2009", "2005", "2004", "1497", "1507", "1817", "2002", "2018"]
d = ['!','#','$','%','^','&','*','-','_','+','=']
z = itertools.chain(itertools.product(a,b,c,d),itertools.product(a,b,d,c),itertools.product(a,b,d,c),itertools.product(a,c,b,d)
,itertools.product(a,c,d,b),itertools.product(a,d,b,c),itertools.product(a,d,c,b),itertools.product(b,a,c,d),itertools.product(b,a,d,c),itertools.product(b,c,a,d),itertools.product(b,c,d,a)
,itertools.product(b,d,a,c),itertools.product(b,d,c,a),itertools.product(c,a,b,d),itertools.product(c,a,d,b),itertools.product(c,b,a,d)
,itertools.product(c,b,d,a),itertools.product(c,d,a,b),itertools.product(c,d,b,a),itertools.product(d,a,b,c)
,itertools.product(d,a,c,b),itertools.product(d,b,a,c),itertools.product(d,b,c,a),itertools.product(d,c,a,b),itertools.product(d,c,b,a))
for i in z:
	print("".join(i))
	file.write("".join(i))
	file.write("\n")
