'''
YouTube Video Engagement Analysis
You are given a list of YouTube video records, where each record is a dictionary with the following keys:

"title" (str)
"views" (int)
"likes" (int)
"comments" (int)
Implement the following functions:

total_engagement(video: dict) -> int
Returns the total engagement (likes + comments) for a given video.
engagement_rate(video: dict) -> float
Returns the engagement rate for a given video, using the formula:
                   likes + comments
Engagement Rate = ------------------  x 100
                        views
If views is 0, return 0.0
Round the result to 2 decimal places
most_engaging_video(videos: list[dict]) -> str
Returns the title of the video with the highest engagement rate. If there is a tie, return the first one in the list.
videos_with_engagement_rate_above_threshold(videos: list[dict], threshold: float) -> list[str]
Returns a list of video titles whose engagement rate is strictly greater than the given threshold.
average_engagement_rate(videos: list[dict]) -> float
Returns the average engagement rate of all videos with non-zero views, rounded to 2 decimal places.
'''
def total_engagement(video: dict) -> int:
    """Returns the total engagement (likes + comments) of a given video."""
    return video.get("likes", 0) + video.get("comments", 0)


def engagement_rate(video: dict) -> float:
    """Returns the engagement rate ((likes + comments) / views) * 100 rounded to 2 decimals. Returns 0.0 if views == 0."""
    views = video.get("views", 0)
    if views == 0:
        return 0.0
    rate = total_engagement(video) / views * 100
    return round(rate, 2)


def most_engaging_video(videos: list) -> str:
    """Returns the title of the video with the highest engagement rate. Returns the first in case of tie."""
    if not videos:
        return ""
    max_rate = -1
    best_title = ""
    for video in videos:
        rate = engagement_rate(video)
        if rate > max_rate:
            max_rate = rate
            best_title = video["title"]
    return best_title


def videos_with_engagement_rate_above_threshold(videos: list, threshold: float) -> list:
    """Returns titles of videos whose engagement rate is strictly greater than the given threshold."""
    result = []
    for video in videos:
        if engagement_rate(video) > threshold:
            result.append(video["title"])
    return result


def average_engagement_rate(videos: list) -> float:
    """Returns the average engagement rate of videos with non-zero views, rounded to 2 decimal places."""
    rates = [engagement_rate(v) for v in videos if v.get("views", 0) > 0]
    if not rates:
        return 0.0
    avg = sum(rates) / len(rates)
    return round(avg, 2)
