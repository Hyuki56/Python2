import numpy as np

# shape : 넘파이 배열의 형태를 나타내는 튜플로 각 차원의 크기를 나타냄
x = np.array([[1,2,3],[4,5,6]])
print(x.shape) # 2행 3열

# dtype : 넘파이 배열의 데이터 타입을 나타냄
print(x.dtype) # int64 타입 ( C언어나 더 큰 프로그래밍 관점으로는 int가 세부적으로 나뉨 )

# size : 넘파이 배열의 전체 요소 수를 나타냄
print(x.size)

# ndim : 넘파이 배열의 차원 수를 나타냄
print(x.ndim) #n차원 dimention 디멘션
x2 = np.array([[[1],[2]],[[3],[4]]])
print(x2.ndim)
print()

# flat : 넘파이 배열 요소들을 1차원 형태로 순회할 수 있는 속성
x = np.array([[1,2],[3,4]])
for e in x.flat:
    print(e)

# 요쇼들의 자료형을 명시하며 넘파이 배열 생성
a = np.array([1,2,3], dtype=np.int32)
print(a.dtype)
b = np.array([True, False, True], dtype=np.bool_) # v(자료형):bool_, c(클래스):bool
print(b.dtype)

# astype() : 데이터 타입 반환
c = a.astype(np.float32)
print(c)
d = np.array([1.1, 2.2, 3.3])
e = a.astype(np.int32)
print(e)
