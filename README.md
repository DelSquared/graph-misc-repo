# Graph Miscellaneous Repository
A miscellaneous repository for anything having to do with computation in the context of Graph Theory

#### Content:
- [1) Network of Squares](https://github.com/DelSquared/graph-misc-repo#1-network-of-squares)
  - [The characteristic polynomials](https://github.com/DelSquared/graph-misc-repo#the-characteristic-polynomials)
  - [The Edge, MinAvgMax-Degree countings](https://github.com/DelSquared/graph-misc-repo#the-edge-minavgmax-degree-countings)
  - [The Graph "Entropy"](https://github.com/DelSquared/graph-misc-repo#the-graph-entropy)
  - [Further Readings](https://github.com/DelSquared/graph-misc-repo#further-readings)
- [2) More Sections Coming Soon](https://github.com/DelSquared/graph-misc-repo#2-more-sections-coming-soon)

## 1) Network of Squares
This section deals with the problem discussed my Matt Parker [here](https://www.youtube.com/watch?v=G1m7goLCJDY), [here](https://www.youtube.com/watch?v=7_ph5djCCnM) and in his book "Things to Make and Do in the Fourth Dimension" with regards to his conjecture: *That all consecutive integer sequences that exceed 25 can be rearranged such that the adjacent numbers sum to a square number, as well as 15, 16, 17, 23.* One natural way to tackle this is using Hamiltonian paths on graphs like Parker did. A brute force search up to 299 was carried out by Charlie Turner and the code can be found [here](https://github.com/charlieturner/square-sum-sequences) where the conjecture was found to hold.

This subsection is currently only serving as a "data collection" centre where various data about such graphs is collected for anyone who needs to do an analysis.

#### The characteristic polynomials
Due to the symbolic nature of the code and the size of the matrices undergoing the operations. I only managed to generate the characteristic polynomials *C* = det(*A* - *xI*) up to a degree of 34 and can be seen [here](https://github.com/DelSquared/graph-misc-repo/blob/master/NetworkOfSquares/VariousResults/CharacteristicPolynomials/graphs-connecting-pairs.pdf). It is curious to note that quite a lot of adjacency matrices are singular (i.e. they are not invertible, det(*A*)=0, the polynomial has a *y*-intercept at 0). It is also interesting how rare odd-valued determinants are, even though the sample size is quite small.

#### The Edge, MinAvgMax-Degree countings
This was by far the easiest exhaustive lists to run. It basically counts the edges on each graph and finds the minimum, average and maximum degrees within the graph. Using the [Handshake Lemma](https://en.wikipedia.org/wiki/Handshaking_lemma) the script was made a bit more efficient by calculating the average degree directly from the number of edges as <sup>2*E*</sup>/<sub>*n*</sub>. The list of the obtained values can be found [here](https://github.com/DelSquared/graph-misc-repo/blob/master/NetworkOfSquares/VariousResults/EdgesAndDegrees/EdgesMinAvgMaxDegree.pdf) as well as a plot of the number of edges as a function of the number of edges.
<p align="center">
  <img src="https://raw.githubusercontent.com/DelSquared/graph-misc-repo/master/NetworkOfSquares/VariousResults/EdgesAndDegrees/PlotOfEAgainstV.png" width="700"/>
</p>

#### The Graph "Entropy"
This result came out of a curiosity I had. Given that the [Shannon Entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)) is given by the sum of terms of the form -*p*log(*p*) or more simply as the expectation **E**[-log(*p*)], imagine being on a vertex *v* and choosing an edge randomly and uniformly (for whatever reason). the probability of choosing each node is *p*=<sup>1</sup>/<sub>deg(*v*)</sub>. Now substituting this into the Shannon Entropy formula we would be summing terms of the form -*p*log(*p*) = <sup>log(deg(*v*))</sup>/<sub>deg(*v*)</sub>. So I decided to investigate how this quantity changes with graph size. A .CSV file with the values can be found [here](https://github.com/DelSquared/graph-misc-repo/blob/master/NetworkOfSquares/VariousResults/Entropy/Graph%20Entropy-like%20functional%20up%20to%201000%20vertices.csv) and I plotted the values up to 500 and up to 1000 vertices.
<p align="center">
  <img src="https://raw.githubusercontent.com/DelSquared/graph-misc-repo/master/NetworkOfSquares/VariousResults/Entropy/Graph%20'Entropy'%20plot%20up%20to%20500%20vertices.png" width="750"/>
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/DelSquared/graph-misc-repo/master/NetworkOfSquares/VariousResults/Entropy/Graph%20'Entropy'%20plot%20up%20to%201000%20vertices.png" width="750"/>
</p>
It is evident that there is some sharp jittering for a low number of vertices and then smooths out for larger values which could be a promising indication that the Hamiltonicity of a graph could have some distant relation with this quantity.

#### Further Readings
- https://github.com/charlieturner/square-sum-sequences
- https://en.wikipedia.org/wiki/Handshaking_lemma
- https://en.wikipedia.org/wiki/Entropy_(information_theory)

## 2) More Sections Coming Soon
