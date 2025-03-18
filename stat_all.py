import statistics

class Stats:
    @staticmethod
    def get_course_statistics(records, course_id):
        grades = [s.courses[course_id][1] for s in records.values() if course_id in s.courses]
        avg_score = sum(grades) / len(grades) if grades else 0
        median_score = statistics.median(grades) if grades else 0
        return avg_score, median_score