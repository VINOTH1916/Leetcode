class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0
        slower_time = 0

        cars = sorted(zip(position,speed), reverse =  True)

        for pos,sp in cars:
            time = (target-pos)/sp

            if time > slower_time:
                fleet += 1
                slower_time = time

        return fleet
    
        