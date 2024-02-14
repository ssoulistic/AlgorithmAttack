def solution(new_id):
    # 1. 소문자
    new_id=new_id.lower()
    # 2. 알파벳 소문자,숫자,빼기,밑줄,마침표만 남기기
    # 3. .. 두번이상 => 하나
    temp=""
    for char in new_id:
        if char.isalpha() or char.isdigit() or char in ["-","_","."]:
            temp+=char
    new_id=temp
    
    while new_id!=new_id.replace("..","."):
        new_id=new_id.replace("..",".")
    
    # 4. . 처음 과 끝 제거
    if len(new_id)>1:
        if new_id[0]==".":
            new_id=new_id[1:]
        if new_id[-1]==".":
            new_id=new_id[:-1]
    else:
        if new_id[0]==".":
            new_id=""
        elif new_id[-1]==".":
            new_id=""
    # 5. 빈문자열이면 a 대입
    if not new_id:
        new_id="a"
    # 6. 16자 이상 => 첫 15문자 남기기 (끝이 .이면 제거)
    if len(new_id)>15:
        new_id=new_id[:15]
        if new_id[-1]==".":
            new_id=new_id[:-1]
    # 7. 2자 이하 => 마지막 문자 3자 될때까지 붙이기.
    while len(new_id)<3:
        new_id=new_id+new_id[-1]
    return new_id