# py-cassandra

## Testing Cassandra on PDS

Need to Demo a few Kubernetes Pods writing data to a Cassandra Data Service on PDS? Don't want to learn YCSB?
Great, you are in the right place. :)

1. Deploy a Cassandra data Service on PDS. After the deployment is ready make sure to grab the Nodes names, Username and Password from the Connection link for the Service in PDS.

2. Clone this repo `git clone git@github.com:2vcps/py-cassandra.git` 

3. Edit `env-secret.yaml` to match your environment. You may need to add more server variables if you have many nodes in Cassandra. If you do add more make sure to also edit `worker.yaml` and `py-cass.py`. Then you will have to do a Dockerbuild of your own image.

4. Apply the worker.yaml to create the deployment.
```
kubectl create ns py-cassandra
kubectl -n py-cassandra apply -f worker.yaml
```

5. Verify your dataservice is working.
```
kubectl -n pds-demo get pod
kubectl -n pds-demo exec -it <cassandra pod> -- bash
```
From the pod:
```
cqlsh

describe keyspaces;
use michael;

```
**Note** *The Python worker will auto create these names don't yell at me if they are funny. Also each instance of the python script will create a new keyspace. The goal was to create data with little effort in checking for existing tables/keyspaces.*
Example handful of keyspaces
```
pds@cqlsh> describe keyspaces;

kathy    richard   system_schema  krista              joyce          jeanne
timothy  cicely    system_auth    brandi              system_traces
mike     kathleen  michael        cindy               lavonne      
carolyn  kyla      system         system_distributed  rebecca 
```

Now try:
```
select * from users;
```
Output:
```
 user_id                              | credits | name
--------------------------------------+---------+----------------------
 bcf73f8c-e82b-11ec-abc3-068694a62d59 |   11723 |         Jean Grenier
 9226674c-e82b-11ec-abc3-068694a62d59 |    1930 |          Alyce Grant
 9c48c2c4-e82b-11ec-abc3-068694a62d59 |    3969 |       Joseph Kennedy
 d2817b24-e82b-11ec-abc3-068694a62d59 |   16049 |   Mary Sciancalepore
 97707b34-e82b-11ec-abc3-068694a62d59 |    2998 |     Kenneth Introini
 8a1009c8-e82b-11ec-abc3-068694a62d59 |     594 |      Armando Obrecht
 af2c0964-e82b-11ec-abc3-068694a62d59 |    8442 |      Stephen Boucher
 a80b56a8-e82b-11ec-abc3-068694a62d59 |    6705 |         John Gaither
 d4808744-e82b-11ec-abc3-068694a62d59 |   16687 |        Jasper Hippen
 b4fd744a-e82b-11ec-abc3-068694a62d59 |    9766 |       Leland Lefevre
 abbc0702-e82b-11ec-abc3-068694a62d59 |    7718 |        David Johnson
 c7a3d012-e82b-11ec-abc3-068694a62d59 |   13921 |     Carl Hockensmith
 8853c066-e82b-11ec-abc3-068694a62d59 |     449 |        Willie Flores
 a33442a2-e82b-11ec-abc3-068694a62d59 |    5732 |        Lewis Barnard
 aa4059b4-e82b-11ec-abc3-068694a62d59 |    7380 |       Joyce Marriott
 b9366cb0-e82b-11ec-abc3-068694a62d59 |   10593 |         Ralph Ackles
 c8bf23ca-e82b-11ec-abc3-068694a62d59 |   14271 |          Tanya Click
 948d4636-e82b-11ec-abc3-068694a62d59 |    2451 |           Mark Bower
 90740d1e-e82b-11ec-abc3-068694a62d59 |    1459 |     Crystal Anderson
 90a662fa-e82b-11ec-abc3-068694a62d59 |    1506 |        Bruce Burgess
 d324bb86-e82b-11ec-abc3-068694a62d59 |   16227 |     Mitchel Dilworth
 91558622-e82b-11ec-abc3-068694a62d59 |    1722 |        Mitchell Rand
 c0f2b3fa-e82b-11ec-abc3-068694a62d59 |   12376 |       Sherrell Litke
 cd1c6bd0-e82b-11ec-abc3-068694a62d59 |   15081 |    Shirley Henderson
 b054e068-e82b-11ec-abc3-068694a62d59 |    8833 |        Harry Shorter
 a3f89ab2-e82b-11ec-abc3-068694a62d59 |    5944 |     Benjamin Handley
 96c20b9e-e82b-11ec-abc3-068694a62d59 |    2779 |     Harold Treadwell
 cfbc9b80-e82b-11ec-abc3-068694a62d59 |   15655 |   Natalie Mccullough
 af65ba10-e82b-11ec-abc3-068694a62d59 |    8526 |        Neil Hamilton
 c3574796-e82b-11ec-abc3-068694a62d59 |   13100 |    Daniel Mcclanahan
 bbe0226c-e82b-11ec-abc3-068694a62d59 |   11347 |    Michael Mcdonough
 cbce2b88-e82b-11ec-abc3-068694a62d59 |   14683 |       Connie Trevino
 d86fcaae-e82b-11ec-abc3-068694a62d59 |   17459 |      Donald Schleich
 cc92bb4c-e82b-11ec-abc3-068694a62d59 |   14877 |  Matthew Christensen
 cc807446-e82b-11ec-abc3-068694a62d59 |   14857 |     Chelsea Ursprung
 b6277ae6-e82b-11ec-abc3-068694a62d59 |   10098 |      Patricia Bowman
 a2552cca-e82b-11ec-abc3-068694a62d59 |    5405 |          Robert Reed
 9699998e-e82b-11ec-abc3-068694a62d59 |    2724 |        Jackie Carter
 af4687bc-e82b-11ec-abc3-068694a62d59 |    8475 |        Albert Lovell
 d384f3e8-e82b-11ec-abc3-068694a62d59 |   16367 |          Adam Sowell
 a9fc3496-e82b-11ec-abc3-068694a62d59 |    7308 |         Beth Bratton
 8d000f02-e82b-11ec-abc3-068694a62d59 |    1063 |        Phyllis Jones
 d5c52a10-e82b-11ec-abc3-068694a62d59 |   16948 | Christopher Rockwell
 a2a18ffc-e82b-11ec-abc3-068694a62d59 |    5540 |           Alan Borja
 a4b96364-e82b-11ec-abc3-068694a62d59 |    6198 |         Timothy Hart
 a7b759a4-e82b-11ec-abc3-068694a62d59 |    6641 |         Carrie Goyco
 bc3b64ba-e82b-11ec-abc3-068694a62d59 |   11491 |        Donald Durham
 c73c2db8-e82b-11ec-abc3-068694a62d59 |   13781 |           Jean White
```

6. You can also scale the worker deployment
```
kubectl -n py-cassandra scale deployment worker-cassandra --replicas=16
```