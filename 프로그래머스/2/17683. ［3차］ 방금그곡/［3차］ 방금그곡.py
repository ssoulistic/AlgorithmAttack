def solution(m, musicinfos):
    conv={"C#":"H","D#":"I","F#":"J","G#":"K","A#":"L","B#":"M"}
    
    def convert(melodies):
        for k,v in conv.items():
            melodies=melodies.replace(k,v)
        return melodies
    m=convert(m)
    
    answer = []
    for idx,info in enumerate(musicinfos):
        start_time,end_time,song_name,song=info.split(",")
        
        hour,minute=start_time.split(":")
        start_time=int(hour)*60+int(minute)
        hour,minute=end_time.split(":")
        end_time=int(hour)*60+int(minute)
        
        run_time=end_time-start_time
        
        song=convert(song)
        song=(song*(run_time//len(song)+1))[:run_time]
        
        if m in song:
            answer.append([-run_time,idx,song_name])
    
    if answer==[]:
        return "(None)"
    else:
        return sorted(answer)[0][2]
