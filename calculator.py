# برنامج حساب الميزانية الشخصية
print("--- مرحباً بك في حاسبة الميزانية البسيطة ---")

# مدخلات المستخدم
salary = float(input("أدخل راتبك الشهري (أو مصروفك): "))
rent = float(input("أدخل تكلفة السكن / الإيجار: "))
food = float(input("أدخل تكلفة الطعام شهرياً: "))
other_expenses = float(input("أدخل أي مصاريف أخرى: "))

# العمليات الحسابية
total_expenses = rent + food + other_expenses
remaining_balance = salary - total_expenses

# المخرجات
print("\n--- التقرير النهائي ---")
print(f"إجمالي مصاريفك: {total_expenses}")

if remaining_balance > 0:
    print(f"عاش! هيتبقى معاك {remaining_balance} لآخر الشهر.")
elif remaining_balance == 0:
    print("ميزانيتك مضبوطة بالظبط، مفيش توفير.")
else:
    print(f"خلي بالك، أنت مديون بـ {abs(remaining_balance)}!")
