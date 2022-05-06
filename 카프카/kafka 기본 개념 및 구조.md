
### Apache kafka란
- Data in motion Platform for enterprise
- 움직이는 데이터를 처리하는 플랫폼
- Event Streaming Platform




### Apache kafka의 특징
- 3가지 주요 특징
  - 이벤트 스트림을 안전하게 전송 (Publish & Subscribe)
  - 이벤트 스트림을 디스크에 저장 (Write to Disk)
  - 이벤트 스트림을 분석 및 처리 (Processing & Ananlysis)

 
<Br>
   
### Apache kafka시스템 구조

  - Topic
    - 토픽은 카프카 클러스터의 브로커에서 데이터를 관리할 때 기준이 되는 개념
    - 데이터를 구분하기 위한 분류값 혹은 구분된 저장소

  - Leader Partition
    - 프로듀서(Producer)로부터 전달된 데이터를 보관하는 역할
    - 리더 파티션은 프로듀서 또는 컨슈머와 직접 통신하는 파티션
    - 프로듀서/컨슈머와 직접 통신함으로써 읽기, 쓰기 연산을 담당
  
  - Follower Partition
    - 프로듀서로부터 리더 파티션으로 전달된 데이터를 복제(replication)하여 복제된 데이터를 저장
    - 리더 파티션이 속해있는 브로커 에러 발생시 리더 파티션의 역할을 할 수 있음
  
  - Replication Factor
    
    - 파티션의 복제 계수 = 1
      - 브로커 A에 리더 파티션만 존재, 브로커 A의 해당 토픽의 파티션이 총 3개 (3개 모두 리더 파티션)
    - 파티션의 복제 계수 = 3
      - A의 파티션의 데이터를 복제해서 가지고 있을 브로커 B, C의 파티션이 존재
  
  
  -  broker
    
    - 브로커(Broker)는 카프카 서버
    - 브로커 내부에 여러 토픽들이 생성될 수 있고 토픽들에 의해 생성된 파티션들이 보관하는 데이터에 대해 분산 저장을 해주거나 장애 발생 시, 안전하게 데이터를 사용할 수 있도록 도와주는 역할
    
    - Controller
      - error가 발생한 브로커의 토픽에 있는 리더 파티션을 같은 클러스터 내의 정상 동작하는 다른 브로커에게 토픽의 리더 파티션 지위를 재분배하는 역할
    
    - Coordinator
        - 코디네이터는 컨슈머 그룹의 상태를 체크 → 컨슈머 그룹 내의 컨슈머가 장애가 발생하여 매칭된 파티션의 데이터를 컨슘(consume)할 수 없는 경우 → error가 발생한 컨슈머에게 매칭된 파티션을 정상 동작하는 다른 컨슈머에게 매칭하여 재할당
        - 파티션을 컨슈머에게 재할당하는 과정을 리밸런스 (Rebalance)
  
  
  - Zookeeper
    - 카프카의 분산 처리 시스템의 서버들에 관한 메타데이터(환경 설정 등)를 통합 관리하는 시스템
    - 설정관리 (Configuration Management)
        - 클러스터의 설정 정보를 최신으로 유지하기 위한 시스템으로 사용
    - 클러스터 관리 (Cluster Management)
        - 클러스터의 서버(브로커)가 추가되거나 제외될 때 그 정보를 클러스터 안 서버(브로커)들이 공유하는데 사용
  - Zookeeper Ensemble
    - 주키퍼의 클러스터
  
  
  
  - Partitioner
    - 파티셔너(Partitioner)는 프로듀서 애플리케이션 내에서 생성된 메시지를 카프카에 보낼 때, 이 메시지가 토픽의 어떤 파티션(Partition)에 전달될 지를 정하는 역할
    - 프로듀서 API를 사용하는 경우, 2개의 파티셔너(Round Robin Partitioner, Uniform Sticky Partitioner)를 제공
    - 차이점
      - 메시지의 key가 없을 때는 파티션에 메시지를 분배하는 로직에 차이가 있음
    - Uniform Sticky Partitioner
      - 데이터가 배치로 모두 묶일 때 까지 기다린 후, 묶여진 데이터 덩어리는 모두 동일한 파티션에 전송함으로써 높은 처리량과 낮은 리소스 사용률을 가지게 됨

  - Producer 
    - 메시지를 생산(produce)해서 카프카의 토픽으로 메시지를 보내는 역할을 하는 애플리케이션, 서버 등을 모두 프로듀서라고 함
    - 프로듀서의 주요 기능은 각각의 메시지를 토픽 파티션에 매핑하고 파티션의 리더에 요청을 보내는 것
  
  
  - Consumer와 Consumer gloup
    - 컨슈머가 토픽을 구독(Subscribe) 혹은 읽는다(Read) → 컨슈머가 토픽 파티션에 저장된 메시지들을 가져오는 것
    - Polling 구조
    - Consumer gloup
  
  
