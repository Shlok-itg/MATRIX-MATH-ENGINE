import numpy as np
from scipy import linalg

def get_input():
    a = list(map(float, input("ENTER THE NUMBERS FOR MATRIX (space-separated): ").split()))
    return np.array(a)

def convert_to_matrix(mat, rows, cols):
    try:
        return mat.reshape((rows, cols))
    except ValueError:
        return f"Error: Cannot reshape {mat.size} elements into a {rows}x{cols} matrix."

def addition(mat1, mat2):
    if mat1.shape != mat2.shape:
        return "MATRIX ADDITION NOT POSSIBLE.... SHAPE MIS-MATCH. TRY AGAIN."
    return mat1 + mat2
    
def subtraction(mat1, mat2):
    if mat1.shape != mat2.shape:
        return "MATRIX SUBTRACTION NOT POSSIBLE.... SHAPE MIS-MATCH. TRY AGAIN."
    return mat1 - mat2
    
def transpose(mat):
    return mat.T  

def multiplication(mat1, mat2):
    if mat1.shape[1] != mat2.shape[0]:
        return "MATRIX MULTIPLICATION NOT POSSIBLE.... INNER DIMENSIONS DO NOT MATCH."
    return np.dot(mat1, mat2)

def trace_of(mat1):
    if mat1.shape[0] != mat1.shape[1]:
        return "TRACE NOT DEFINED"
    return np.trace(mat1)

def scalar_multiplication(mat1, a):
    return a * mat1

def compute_eigen_value(mat):
    if mat.shape[0] != mat.shape[1]:
        return "MATRIX IS NOT SQUARE... EIGEN VALUE NOT DEFINED"
    return linalg.eigvals(mat)
    
def compute_eigen_vector(mat):
    if mat.shape[0] != mat.shape[1]:
        return "MATRIX IS NOT SQUARE... EIGEN VECTORS ARE NOT DEFINED"
    _, ans = linalg.eig(mat) 
    return ans
    
def inverse_of(mat):
    if mat.shape[0] != mat.shape[1]:
        return "MATRIX IS NOT SQUARE... INVERSE NOT DEFINED"
    if np.isclose(linalg.det(mat), 0):
        return "MATRIX IS NOT INVERTIBLE"
    return linalg.inv(mat)

def solve_equations(mat1, mat2): 
    if mat1.shape[0] != mat1.shape[1]:
        return "COEFFICIENT MATRIX MUST BE SQUARE."
    
    if mat1.shape[0] != mat2.shape[0]: 
        return "DIMENSION MISMATCH: ROWS OF MAT1 MUST EQUAL ROWS OF MAT2."
    return linalg.solve(mat1, mat2)

def rank_of(mat):
    return np.linalg.matrix_rank(mat)

def lu_decomposition(mat):
    try:
        P, L, U = linalg.lu(mat)
        return P, L, U
    except ValueError:
        return "LU DECOMPOSITION FAILED. CHECK MATRIX DIMENSIONS."
    
a=1
while a:
    print("SIMPLE MATRIX MATH ENGINE:\n")     
    print("ENTER THE SHAPE OF MATRIX A (rows x columns):\n")
    a1,b1=map(int ,input().split())
    print("ENTER SHAPE OF MATRIX B (axb):\n")
    a2,b2=map(int ,input().split())
    
    arr1= get_input()
    arr2= get_input()
    
    mat1=convert_to_matrix(arr1, a1,b1)
    mat2=convert_to_matrix(arr2,a2,b2)
    print(mat1)
    print(mat2)
    print("\n=======================================================================\n")
    print("BELOW ARE THE AVAILABLE OPTIONS FOR THE MATRIX MATH:\n")
    print("1. ADDITION\n")
    print("2. SUBTRACTION \n")
    print("3. TRANSPOSE\n")
    print("4. MULTIPLICATION \n")
    print("5. COMPUTE TRACE OF MATRIX\n")
    print("6. MULTIPLICATION BY SCALAR\n")
    print("7. COMPUTE EIGEN VALUES\n")
    print("8. COMPUTE EIGEN VECTORS\n")
    print("9. COMPUTE INVERSE OF MATRIX\n")
    print("10. SOLVE A SYSTEM OF EQUATION (mat1 * X=mat2)\n")
    print("11. COMPUTE RANK OF MATRIX\n")
    print("12. CALCULATE L-U DECOMPOSITION\n")
    
    while True:
        try:
            print("\n" + "="*71)
            choice = int(input("ENTER YOUR CHOICE (1-12) OR 0 TO EXIT: "))
        except ValueError:
            print("\nINVALID INPUT. PLEASE ENTER A NUMBER.")
            continue
    
        if choice == 0:
            print("\nEXITING THE MATH ENGINE. GOODBYE!")
            break
            
        elif choice == 1:
            print("\nRESULT OF ADDITION:\n", addition(mat1, mat2))
            
        elif choice == 2:
            print("\nRESULT OF SUBTRACTION:\n", subtraction(mat1, mat2))
            
        elif choice == 3:
            mat_choice = input("WHICH MATRIX? (A/B): ").strip().upper()
            if mat_choice == 'A':
                print("\nTRANSPOSE OF A:\n", transpose(mat1))
            elif mat_choice == 'B':
                print("\nTRANSPOSE OF B:\n", transpose(mat2))
            else:
                print("INVALID CHOICE.")
                
        elif choice == 4:
            print("\nRESULT OF MULTIPLICATION:\n", multiplication(mat1, mat2))
            
        elif choice == 5:
            mat_choice = input("WHICH MATRIX? (A/B): ").strip().upper()
            if mat_choice == 'A':
                print("\nTRACE OF A:\n", trace_of(mat1))
            elif mat_choice == 'B':
                print("\nTRACE OF B:\n", trace_of(mat2))
            else:
                print("INVALID CHOICE.")
                
        elif choice == 6:
            mat_choice = input("WHICH MATRIX? (A/B): ").strip().upper()
            if mat_choice in ['A', 'B']:
                try:
                    scalar = float(input("ENTER THE SCALAR VALUE: "))
                    if mat_choice == 'A':
                        print("\nSCALAR MULTIPLICATION OF A:\n", scalar_multiplication(mat1, scalar))
                    else:
                        print("\nSCALAR MULTIPLICATION OF B:\n", scalar_multiplication(mat2, scalar))
                except ValueError:
                    print("INVALID SCALAR VALUE.")
            else:
                print("INVALID CHOICE.")
                
        elif choice == 7:
            mat_choice = input("WHICH MATRIX? (A/B): ").strip().upper()
            if mat_choice == 'A':
                print("\nEIGEN VALUES OF A:\n", compute_eigen_value(mat1))
            elif mat_choice == 'B':
                print("\nEIGEN VALUES OF B:\n", compute_eigen_value(mat2))
            else:
                print("INVALID CHOICE.")
                
        elif choice == 8:
            mat_choice = input("WHICH MATRIX?(A/B): ").strip().upper()
            if mat_choice == 'A':
                print("\nEIGEN VECTORS OF A:\n", compute_eigen_vector(mat1))
            elif mat_choice == 'B':
                print("\nEIGEN VECTORS OF B:\n", compute_eigen_vector(mat2))
            else:
                print("INVALID CHOICE.")
                
        elif choice == 9:
            mat_choice = input("WHICH MATRIX? (A/B): ").strip().upper()
            if mat_choice == 'A':
                print("\nINVERSE OF A:\n", inverse_of(mat1))
            elif mat_choice == 'B':
                print("\nINVERSE OF B:\n", inverse_of(mat2))
            else:
                print("INVALID CHOICE.")
                
        elif choice == 10:
            print("\nSOLVING SYSTEM OF EQUATIONS (A * X = B):\n", solve_equations(mat1, mat2))
            
        elif choice == 11:
            mat_choice = input("WHICH MATRIX? (A/B): ").strip().upper()
            if mat_choice == 'A':
                print("\nRANK OF A:\n", rank_of(mat1))
            elif mat_choice == 'B':
                print("\nRANK OF B:\n", rank_of(mat2))
            else:
                print("INVALID CHOICE.")
                
        elif choice == 12:
            mat_choice = input("WHICH MATRIX? (A/B): ").strip().upper()
            if mat_choice == 'A':
                res = lu_decomposition(mat1)
                if isinstance(res, tuple):
                    print("\nL-U DECOMPOSITION OF A:\nP=\n", res[0], "\nL=\n", res[1], "\nU=\n", res[2])
                else:
                    print("\n" + res)
            elif mat_choice == 'B':
                res = lu_decomposition(mat2)
                if isinstance(res, tuple):
                    print("\nL-U DECOMPOSITION OF B:\nP=\n", res[0], "\nL=\n", res[1], "\nU=\n", res[2])
                else:
                    print("\n" + res)
            else:
                print("INVALID CHOICE.")
                
        else:
            print("\nINVALID OPTION. PLEASE SELECT A NUMBER BETWEEN 1 AND 12.")

    ch= input("DO YOU WANT TO USE THE ENGINE AGAIN?(Y/N): ")
    if ch=="N":
        print("THANKS FOR USING THE MATRIX ENGINE...\n==================================\n")
        break
    elif ch=="Y":
        print("===================================================================\n")
        a=1