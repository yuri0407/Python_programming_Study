#딕셔너리 생성
student1 = {"학번" : 1000, "이름" : "홍길동", "학과" : "컴퓨터학과"}

#딕셔너리 추가
student1["연락처"] = "010-1111-2222"

#딕셔너리 수정
student1["학과"] = "파이썬학과"

#딕셔너리 삭제
del(student1["학과"])

#동일한 키를 갖는 딕셔너리를 생성하는 것이 아니라 마지막에 있는 키가 적용
student2 = {"학번" : 1000, "이름" : "홍길동", "학과" : "파이썬학과", "학번" : 2000}
print(student1)

#딕셔너리의 사용
student1["학번"]
student1["이름"]
student2["학과"]

student1.get("이름")

#딕셔너리명.keys()는 딕셔너리의 모든 키 반환
student1.keys()

#딕셔너리명.values() 함수는 딕셔너리의 모든 값을 리스트로 만들어 반환
student1.values()

#딕셔너리명.items() 함수를 사용하면 튜플 형태로도 구할 수 있음
student1.items()

#딕셔너리 안에 해당 키가 있으면 true, 없으면 false
"이름" in student1
"주소" in student1