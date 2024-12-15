def selection_sort(marks):
    for i in range(len(marks)):
        min_idx = i
        for j in range(i + 1, len(marks)):
            if marks[min_idx] > marks[j]:
                min_idx = j
        marks[i], marks[min_idx] = marks[min_idx], marks[i]
    return marks

def bubble_sort(marks):
    n = len(marks)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if marks[j] > marks[j + 1]:
                marks[j], marks[j + 1] = marks[j + 1], marks[j]
    return marks

def top_five_marks(marks):
    print("Top marks are:")
    print(*marks[::-1][:5], sep="\n")

def main():
    marks = []
    n = int(input("Enter number of students whose marks are to be displayed: "))
    print("Enter marks for", n, "students (Press ENTER after every student's marks): ")
    for _ in range(n):
        ele = int(input())
        marks.append(ele)
    
    print("The marks of", n, "students are:")
    print(marks)
    
    while True:
        print("\n---------------MENU---------------")
        print("1. Selection Sort of the marks")
        print("2. Bubble Sort of the marks")
        print("3. Exit")
        ch = int(input("\nEnter your choice (from 1 to 3): "))
        
        if ch == 1:
            sorted_marks = selection_sort(marks[:])
            print("Marks after Selection Sort:")
            print(sorted_marks)
            a = input("\nDo you want to display top marks from the list (yes/no): ")
            if a.lower() == 'yes':
                top_five_marks(sorted_marks)
        
        elif ch == 2:
            sorted_marks = bubble_sort(marks[:])
            print("Marks after Bubble Sort:")
            print(sorted_marks)
            a = input("\nDo you want to display top five marks from the list (yes/no): ")
            if a.lower() == 'yes':
                top_five_marks(sorted_marks)
        
        elif ch == 3:
            print("\nThanks for using this program!")
            break
        
        else:
            print("\nEnter a valid choice!")

if __name__ == "__main__":
    main()

