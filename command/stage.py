from imports import *

def get_file_stage():
    stage = random.randint(0, 16) #0~16
    if stage == 0: #0が出たとき
        stageimg="stage1.jpg"
        file = discord.File(fp="stage/stage1.jpg",filename=stageimg,spoiler=False)
    elif stage == 1: #1が出たとき
        stageimg="stage2.jpg"
        file = discord.File(fp="stage/stage2.jpg",filename=stageimg,spoiler=False)
    elif stage == 2: #2が出たとき
        stageimg="stage3.jpg"
        file = discord.File(fp="stage/stage3.jpg",filename=stageimg,spoiler=False)
    elif stage == 3: #3が出たとき
        stageimg="stage4.jpg"
        file = discord.File(fp="stage/stage4.jpg",filename=stageimg,spoiler=False)    
    elif stage == 4: #4が出たとき
        stageimg="stage5.jpg"
        file = discord.File(fp="stage/stage5.jpg",filename=stageimg,spoiler=False)
    elif stage == 5: #5が出たとき
        stageimg="stage6.jpg"
        file = discord.File(fp="stage/stage6.jpg",filename=stageimg,spoiler=False)
    elif stage == 6: #6が出たとき
        stageimg="stage7.jpg"
        file = discord.File(fp="stage/stage7.jpg",filename=stageimg,spoiler=False)
    elif stage == 7: #1が出たとき
        stageimg="stage8.jpg"
        file = discord.File(fp="stage/stage8.jpg",filename=stageimg,spoiler=False)
    elif stage == 8: #1が出たとき
        stageimg="stage9.jpg"
        file = discord.File(fp="stage/stage9.jpg",filename=stageimg,spoiler=False)    
    elif stage == 9: #1が出たとき
        stageimg="stage10.jpg"
        file = discord.File(fp="stage/stage10.jpg",filename=stageimg,spoiler=False)    
    elif stage == 10: #1が出たとき
        stageimg="stage11.jpg"
        file = discord.File(fp="stage/stage11.jpg",filename=stageimg,spoiler=False)    
    elif stage == 11: #1が出たとき
        stageimg="stage12.jpg"
        file = discord.File(fp="stage/stage12.jpg",filename=stageimg,spoiler=False)    
    elif stage == 12: #1が出たとき
        stageimg="stage13.jpg"
        file = discord.File(fp="stage/stage13.jpg",filename=stageimg,spoiler=False)  
    elif stage == 13: #1が出たとき
        stageimg="stage14.jpg"
        file = discord.File(fp="stage/stage14.jpg",filename=stageimg,spoiler=False)    
    elif stage == 14: #1が出たとき
        stageimg="stage15.jpg"
        file = discord.File(fp="stage/stage15.jpg",filename=stageimg,spoiler=False)    
    elif stage == 15: #1が出たとき
        stageimg="stage16.jpg"
        file = discord.File(fp="stage/stage16.jpg",filename=stageimg,spoiler=False)    
    elif stage == 16: #1が出たとき
        stageimg="stage17.jpg"
        file = discord.File(fp="stage/stage17.jpg",filename=stageimg,spoiler=False)    
    else: #それ以外なのでERRORが出た時に処理される
        print("sutageエラー")
    return file