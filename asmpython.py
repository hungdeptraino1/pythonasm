import os

#tên
name = str(input('Enter your name: '))
#hàm tính toán gpa
def calculate_gpa(component_scores):
    #gán các giá trị từ bộ thành phần cho các biến điểm và tín chỉ tương ứng
    total_credits = 0
    weighted_sum = 0
    
    for i in component_scores:

        grade = i[0]
        credits = i[1]
        #khi nhập sai kiểu dữ liệu sẽ được nhắc và cho nhập lại giá trị
        if not isinstance(grade, (int, float)) or not isinstance(credits, (int, float)):
            raise ValueError("The number of subjects and credits must be natural numbers and your score must be a number!")
        #tích lũy tổng số tín chỉ và tổng điểm và tín chỉ tương ứng
        total_credits += credits
        weighted_sum += grade * credits
    #khi có giá trị tín = 0 sẽ báo lỗi
    if total_credits == 0:
        raise ZeroDivisionError("Total credits cannot be zero.")
    #tính toán gpa
    gpa = weighted_sum / total_credits
    return gpa

#hàm để in ra màn hình kết quả gpa
def print_gpa(gpa):
    print(f"Your GPA is: {gpa:.2f}")

#hàm chính tổng hợp lại các hàm ở trên và in ra tệp văn bản
def main():
    try:
        #list điểm thành phần 
        component_scores = []
        #số lượng môn học
        num_subject = int(input("Enter the number of subjects: "))
        #nhập điểm và tín chỉ rồi mở rộng list điểm thành phần
        for i in range(num_subject):
            grade = float(input(f'Enter the grade of the subject {i+1}: '))
            credits = float(input(f'Enter the number of credits of the {i+1} subject: '))
            component_scores.append((grade, credits))
        #sử dụng hàm tính gpa và hàm in ra màn hình ở trên
        gpa = calculate_gpa(component_scores)
        print_gpa(gpa)

        #tạo thư mục
        os.makedirs("C:/Resultsgpa_asm", exist_ok=True)
        #tạo và ghi file
        results=[f'Name: {name}',f'grade and credits: {component_scores}',f'Gpa: {gpa}']
        with open(os.path.join("C:/Resultsgpa_asm", "results.txt"), mode='w') as f:
            f.write(f'{results}')
            print('Your results have been saved to C:/Resultsgpa_asm/results.txt!')       
    #khi có lỗi giá trị hoặc đầu vào
    except ValueError:
        print(f"Error")
    #khi có lỗi chia cho 0
    except ZeroDivisionError:
        print(f"Error number of subject and credits cannot be zero")
main()





