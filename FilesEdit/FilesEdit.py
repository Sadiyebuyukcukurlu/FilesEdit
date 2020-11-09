import os

Source = os.getcwd() #Getcwd:İçinde bulunduğumuz klasörü döndüren bir fonksiyondur.
Files = os.listdir(Source) #Listdir:Bir dizin içindeki dosya ve klasörleri listeleme imkanı verir. 

for File in Files:
	if File.endswith(".txt"): #dosyanın uzantısı .txt ile bitiyor ise bulunması gereken klasör e taşır.
		Target_File = Source + "/txt_Files/";

		if not os.path.isdir(Target_File): #Klasör yok ise olusturur.
			os.mkdir(Target_File)
		
			os.rename(Source + "/" + File, Target_File + File);

	elif File.endswith(".ppt"):
		Target_File = Source + "/ppt_Files/";

		if not os.path.isdir(Target_File):
			os.mkdir(Target_File)

		os.rename(Source + "/" + File, Target_File + File);

	elif File.endswith(".docx"):
#Bir karakter dizisinin hangi karakter dizisi ile bittiğini sorgulayabilir.
		Target_File = Source + "/docx_Files/";
		if not os.path.isdir(Target_File):
#İsdir:Parametre olarak verilen öğenin bir dizin olup olmadığını sorgular
			os.mkdir(Target_File)
#Mkdir:Yeni dizinler oluşturabilmemizi sağlar.
		os.rename(Source + "/" + File, Target_File + File);
#Rename:Dizinlerin adlarını değiştirebiliriz.
