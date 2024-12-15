function solution(chicken) {
    let serviceChicken = 0; // 받을 수 있는 서비스 치킨 수
    let coupons = chicken; // 초기 쿠폰 수는 주문한 치킨 수와 동일

    while (coupons >= 10) { // 쿠폰이 10장 이상일 때만 서비스 치킨을 받을 수 있음
        let newChicken = Math.floor(coupons / 10); // 서비스 치킨 수
        serviceChicken += newChicken; // 총 서비스 치킨 수에 추가
        coupons = coupons % 10 + newChicken; // 남은 쿠폰 + 새로 받은 치킨의 쿠폰
    }

    return serviceChicken; // 총 서비스 치킨 수 반환
}
