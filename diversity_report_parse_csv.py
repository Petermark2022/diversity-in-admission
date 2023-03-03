import csv
import sqlite3

con = sqlite3.connect("diversity_report_data.db")
cur = con.cursor()

con.execute("DROP TABLE IF EXISTS schools")
con.execute("DROP TABLE IF EXISTS enrollments")
print("Tables dropped successfully")

con.execute("CREATE TABLE schools (school_id INTEGER PRIMARY KEY AUTOINCREMENT, process TEXT, dbn TEXT, school_name TEXT, program_code TEXT, program_name TEXT, admission_method TEXT, diversity_in_admission TEXT, selection_criteria TEXT)")
con.execute("CREATE TABLE enrollments (enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT, school_id INTEGER, category TEXT, year TEXT, total_enrollment TEXT, female TEXT, male TEXT, asia TEXT, black TEXT, hispanic TEXT, other TEXT, white TEXT, spanish TEXT, chinese TEXT, bengali TEXT, arabic TEXT, haitian TEXT, french TEXT, russian TEXT, korean TEXT, urdu TEXT, maths_level TEXT, FOREIGN KEY(school_id) REFERENCES schools(school_id))")
print("Tables created successfully")

with open("2020_-_2021_Diversity_Report.csv", newline="") as file_data:
    reader = csv.reader(file_data, delimiter=",")
    next(reader)
    for row in reader:
        print(row)

        process = row[0]
        dbn = row[1]
        school_name = row[2]
        program_code = row[3]
        program_name = row[4]
        admission_method = row[5]
        diversity_in_admission = row[6]
        selection_criteria = row[7]

        cur.execute("INSERT INTO schools VALUES (NULL,?,?,?,?,?,?,?,?)", (process, dbn, school_name, program_code, program_name, admission_method, diversity_in_admission, selection_criteria))
        con.commit()
    print("Data parsed successfully")

with open("2018_Diversity_Report_-_Grades_K-8_Special_Programs.csv", newline="") as data_file:
    reader = csv.reader(data_file, delimiter=",")
    next(reader)
    for row in reader:
        enrollment_id = row[0]

        cur.execute("SELECT school_id from schools WHERE dbn=?", (enrollment_id,))
        school_id_row = cur.fetchone()
        if school_id_row is not None:
            school_id = school_id_row[0]
        else:
            continue

        category = row[3]
        year = row[4]
        total_enrollment = row[5]
        female = row[15]
        male = row[17]
        asia = row[19]
        black = row[21]
        hispanic = row[23]
        other = row[25]
        white = row[27]
        spanish = row[29]
        chinese = row[31]
        bengali = row[33]
        arabic = row[35]
        haitian = row[37]
        french = row[39]
        russian = row[41]
        korean = row[43]
        urdu = row[45]
        maths_level = row[69]

        cur.execute("INSERT INTO enrollments (school_id, category, year, total_enrollment, female, male, asia, black, hispanic, other, white, spanish, chinese, bengali, arabic, haitian, french, russian, korean, urdu, maths_level) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (school_id, category, year, total_enrollment, female, male, asia, black, hispanic, other, white, spanish, chinese, bengali, arabic, haitian, french, russian, korean, urdu, maths_level))
        con.commit()
    else:
        next(reader)
print("Data parsed successfully")

con.close()