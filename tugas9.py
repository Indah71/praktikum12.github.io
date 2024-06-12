def create_stack(n):
    stack = {"elements": [], "size": n}
    return stack

def is_empty(stack):
    return len(stack["elements"]) == 0

def is_full(stack):
    return len(stack["elements"]) == stack["size"]

def push(stack, element):
    if is_full(stack):
        print("Tumpukan penuh!")
    else:
        stack["elements"].append(element)

def pop(stack):
    if is_empty(stack):
        print("Tumpukan kosong!")
    else:
        return stack["elements"].pop()

def print_stack(stack):
    print("Tumpukan:", stack["elements"])

def main():
    n = int(input("Masukkan jumlah elemen tumpukan: "))
    stack = create_stack(n)

    while True:
        print("\nMenu:")
        print("1. Tambah elemen")
        print("2. Kurangi elemen")
        print("3. Cetak tumpukan")
        print("4. Keluar")

        choice = int(input("Pilih menu: "))

        if choice == 1:
            element = int(input("Masukkan elemen: "))
            push(stack, element)
        elif choice == 2:
            pop(stack)
        elif choice == 3:
            print_stack(stack)
        elif choice == 4:
            break
        else:
            print("Menu tidak valid!")

if __name__ == "__main__":
    main()def create_stack(n):
    stack = {"elements": [], "size": n}
    return stack

def is_empty(stack):
    return len(stack["elements"]) == 0

def is_full(stack):
    return len(stack["elements"]) == stack["size"]

def push(stack, element):
    if is_full(stack):
        print("Tumpukan penuh!")
    else:
        stack["elements"].append(element)

def pop(stack):
    if is_empty(stack):
        print("Tumpukan kosong!")
    else:
        return stack["elements"].pop()

def print_stack(stack):
    print("Tumpukan:", stack["elements"])

def main():
    n = int(input("Masukkan jumlah elemen tumpukan: "))
    stack = create_stack(n)

    while True:
        print("\nMenu:")
        print("1. Tambah elemen")
        print("2. Kurangi elemen")
        print("3. Cetak tumpukan")
        print("4. Keluar")

        choice = int(input("Pilih menu: "))

        if choice == 1:
            element = int(input("Masukkan elemen: "))
            push(stack, element)
        elif choice == 2:
            pop(stack)
        elif choice == 3:
            print_stack(stack)
        elif choice == 4:
            break
        else:
            print("Menu tidak valid!")

if __name__ == "__main__":
    main()