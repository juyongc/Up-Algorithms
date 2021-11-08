def solution(genres, plays):
    answer = []
    
    m_genre = dict()    # 가장 많이 재생된 장르 딕셔너리
    m_song = dict()     # 장르별 재생 노래 딕셔너리
    
    for i in range(len(genres)):
        genre = genres[i]   # 현재 장르
        play = plays[i]     # 현재 재생된 횟수
        
        if genre not in m_genre:    # 장르별 총 재생횟수 갱신
            m_genre[genre] = play
        else:
            m_genre[genre] += play
            
        if genre not in m_song:     # 장르별 고유 노래 재생 횟수 및 번호
            m_song[genre] = [(play,i)]
        else:
            m_song[genre].append((play,i))
    # 가장 많이 재생된 횟수로 장르 정렬
    m_genre = sorted(m_genre, key=lambda x : -m_genre[x])
    
    for genre in m_genre:   # 장르별
        now = m_song[genre] # 현재 장르별 고유 노래 재생 횟수 및 번호 정렬
        now.sort(key = lambda x: (-x[0], x[1]))
        # answer에 최대 2개 append
        if len(now) == 1:
            answer.append(now[0][1])
        else:
            answer.append(now[0][1])
            answer.append(now[1][1])
    
    return answer