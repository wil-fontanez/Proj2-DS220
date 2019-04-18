import csv
import redis
# create redis db
r = redis.Redis(host='localhost', port=6379, db=0)
# stores data from USvideos.csv
with open('USvideos.csv', encoding='utf-8') as usData:
    readCSV = csv.reader(usData, delimiter=',')
    for row in readCSV:
        videoID = row[0]
        trendingDate = row[1]
        titleName = row[2]
        channelTitle = row[3]
        categoryID = row[4]
        publishTime = row[5]
        tag = row[6]
        view = row[7]
        like = row[8]
        dislike = row[9]
        commentCount = row[10]
        thumbnailLink = row[11]
        commentsDisabled = row[12]
        ratingsDisabled = row[13]
        videoErrorOrRemoved = row[14]
        description = row[15]
        video = dict(Trending_Date=str(trendingDate), Title=str(titleName), channeltitle=str(channelTitle),
                        categoryid=str(categoryID),
                        publishtime=str(publishTime), Tag=str(tag), viewCount=str(view), likeCount=str(like),
                        dislikecount=str(dislike),
                        comments=str(commentCount), thumbnaillink=str(thumbnailLink),
                        commentDisabled=str(commentsDisabled),
                        ratingdisabled=str(ratingsDisabled), viderrororremoved=str(videoErrorOrRemoved),
                        Description=str(description))
        r.hmset(videoID, video)

# stores data from CAvideos.csv
with open('CAvideos.csv', encoding='utf-8') as caData:
    readCSV = csv.reader(caData, delimiter=',')
    for row in readCSV:
        videoID = row[0]
        trendingDate = row[1]
        titleName = row[2]
        channelTitle = row[3]
        categoryID = row[4]
        publishTime = row[5]
        tag = row[6]
        view = row[7]
        like = row[8]
        dislike = row[9]
        commentCount = row[10]
        thumbnailLink = row[11]
        commentsDisabled = row[12]
        ratingsDisabled = row[13]
        videoErrorOrRemoved = row[14]
        description = row[15]
        video = dict(Trending_Date=str(trendingDate), Title=str(titleName), channeltitle=str(channelTitle),
                        categoryid=str(categoryID),
                        publishtime=str(publishTime), Tag=str(tag), viewCount=str(view), likeCount=str(like),
                        dislikecount=str(dislike),
                        comments=str(commentCount), thumbnaillink=str(thumbnailLink),
                        commentDisabled=str(commentsDisabled),
                        ratingdisabled=str(ratingsDisabled), viderrororremoved=str(videoErrorOrRemoved),
                        Description=str(description))
        r.hmset(videoID, video)
# stores data from DEvideos
with open('DEvideos.csv', encoding='utf-8') as deData:
    readCSV = csv.reader(deData, delimiter=',')
    for row in readCSV:
        videoID = row[0]
        trendingDate = row[1]
        titleName = row[2]
        channelTitle = row[3]
        categoryID = row[4]
        publishTime = row[5]
        tag = row[6]
        view = row[7]
        like = row[8]
        dislike = row[9]
        commentCount = row[10]
        thumbnailLink = row[11]
        commentsDisabled = row[12]
        ratingsDisabled = row[13]
        videoErrorOrRemoved = row[14]
        description = row[15]
        video = dict(Trending_Date=str(trendingDate), Title=str(titleName), channeltitle=str(channelTitle),
                        categoryid=str(categoryID),
                        publishtime=str(publishTime), Tag=str(tag), viewCount=str(view), likeCount=str(like),
                        dislikecount=str(dislike),
                        comments=str(commentCount), thumbnaillink=str(thumbnailLink),
                        commentDisabled=str(commentsDisabled),
                        ratingdisabled=str(ratingsDisabled), viderrororremoved=str(videoErrorOrRemoved),
                        Description=str(description))
        r.hmset(videoID, video)
# stores data from FRvideos
with open('FRvideos.csv', encoding='utf-8') as frData:
    readCSV = csv.reader(frData, delimiter=',')
    for row in readCSV:
        videoID = row[0]
        trendingDate = row[1]
        titleName = row[2]
        channelTitle = row[3]
        categoryID = row[4]
        publishTime = row[5]
        tag = row[6]
        view = row[7]
        like = row[8]
        dislike = row[9]
        commentCount = row[10]
        thumbnailLink = row[11]
        commentsDisabled = row[12]
        ratingsDisabled = row[13]
        videoErrorOrRemoved = row[14]
        description = row[15]
        video = dict(Trending_Date=str(trendingDate), Title=str(titleName), channeltitle=str(channelTitle),
                        categoryid=str(categoryID),
                        publishtime=str(publishTime), Tag=str(tag), viewCount=str(view), likeCount=str(like),
                        dislikecount=str(dislike),
                        comments=str(commentCount), thumbnaillink=str(thumbnailLink),
                        commentDisabled=str(commentsDisabled),
                        ratingdisabled=str(ratingsDisabled), viderrororremoved=str(videoErrorOrRemoved),
                        Description=str(description))
        r.hmset(videoID, video)
with open('GBvideos.csv', encoding='utf-8') as gbData:
    readCSV = csv.reader(gbData, delimiter=',')
    for row in readCSV:
        videoID = row[0]
        trendingDate = row[1]
        titleName = row[2]
        channelTitle = row[3]
        categoryID = row[4]
        publishTime = row[5]
        tag = row[6]
        view = row[7]
        like = row[8]
        dislike = row[9]
        commentCount = row[10]
        thumbnailLink = row[11]
        commentsDisabled = row[12]
        ratingsDisabled = row[13]
        videoErrorOrRemoved = row[14]
        description = row[15]
        video = dict(Trending_Date=str(trendingDate), Title=str(titleName), channeltitle=str(channelTitle),
                        categoryid=str(categoryID),
                        publishtime=str(publishTime), Tag=str(tag), viewCount=str(view), likeCount=str(like),
                        dislikecount=str(dislike),
                        comments=str(commentCount), thumbnaillink=str(thumbnailLink),
                        commentDisabled=str(commentsDisabled),
                        ratingdisabled=str(ratingsDisabled), viderrororremoved=str(videoErrorOrRemoved),
                        Description=str(description))
        r.hmset(videoID, video)
# stores data from INvideos
with open('INvideos.csv', encoding='utf-8') as inData:
    readCSV = csv.reader(inData, delimiter=',')
    for row in readCSV:
        videoID = row[0]
        trendingDate = row[1]
        titleName = row[2]
        channelTitle = row[3]
        categoryID = row[4]
        publishTime = row[5]
        tag = row[6]
        view = row[7]
        like = row[8]
        dislike = row[9]
        commentCount = row[10]
        thumbnailLink = row[11]
        commentsDisabled = row[12]
        ratingsDisabled = row[13]
        videoErrorOrRemoved = row[14]
        description = row[15]
        video = dict(Trending_Date=str(trendingDate), Title=str(titleName), channeltitle=str(channelTitle),
                        categoryid=str(categoryID),
                        publishtime=str(publishTime), Tag=str(tag), viewCount=str(view), likeCount=str(like),
                        dislikecount=str(dislike),
                        comments=str(commentCount), thumbnaillink=str(thumbnailLink),
                        commentDisabled=str(commentsDisabled),
                        ratingdisabled=str(ratingsDisabled), viderrororremoved=str(videoErrorOrRemoved),
                        Description=str(description))
        r.hmset(videoID, video)
# allow queries for all data from a video given video key enter -1 to stop
videoKey = ""
while videoKey != "-1":
    videoKey=input("videokey")
    print(r.hgetall(videoKey))
