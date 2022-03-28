def solution(m, musicinfos):
    answer = ''
    music_start = 9999999
    play_time = 0
    m_list = []
    m = m.replace("C#","X")
    m = m.replace("D#","Y")
    m = m.replace("F#","Z")
    m = m.replace("G#","M")
    m = m.replace("A#","N")
    
    for info in musicinfos:
        s,e,name,score = info.split(",")
        sh,sm = map(int,s.split(":"))
        eh,em = map(int,e.split(":"))
        st = 60*sh + sm
        et = 60*eh + em
        period = et - st
        score = score.replace("C#","X")
        score = score.replace("D#","Y")
        score = score.replace("F#","Z")
        score = score.replace("G#","M")
        score = score.replace("A#","N")
        
        share,rem = divmod(period,len(score))
        # 재생기간별 악보 늘리기,줄이기
        if share > 0:
            music_tot = 2 * (share+1) * score
        else:
            music_tot = score[:rem]
        # 조건 일치 여러 개 => 재생 시간 긴 거, 먼저 입력된 거
        if m in music_tot:
            if play_time < period:
                answer = name
                music_start = st
                play_time = period
            elif play_time == period and music_start > st:
                answer = name
                music_start = st
                play_time = period
                
    if answer == "":
        answer = "(None)"
    return answer