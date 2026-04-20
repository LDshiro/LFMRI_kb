# Gradient and Shim Coil Design Papers Since 1990

Last checked: 2026-04-20

This file is a curated research-paper list for gradient-coil design, shim-coil design, and closely related B0 field-control hardware after 1990. It is not guaranteed to be exhaustive. I prioritized records with DOI and a publisher, PubMed, PubMed Central, or comparable source link.

**Abstract note:** Long publisher abstracts are often copyrighted. Therefore the “Abstract (EN)” and “アブストラクト（JA）” fields below are paraphrased summaries based on the paper records and abstracts, not verbatim copies.

**Abbreviations:** MRI = Magnetic Resonance Imaging; NMR = Nuclear Magnetic Resonance; B0 = main static magnetic field; RF = radio frequency; ROI = region of interest; DSV = diameter spherical volume; UHF = ultra-high field; PNS = peripheral nerve stimulation; LP = linear programming; BEM = boundary element method; FEM = finite element method; FD = finite difference; SVD = singular value decomposition; SH = spherical harmonic.

## Overview table

| ID | Area | Publication time | Title | DOI |
|---|---|---:|---|---|
| G01 | Gradient | 1991 Jan | Gradient coil design using active magnetic screening | [`10.1002/mrm.1910170105`](https://doi.org/10.1002/mrm.1910170105) |
| G02 | Gradient | 1991 Sep | Coil optimization for MRI by conjugate gradient descent | [`10.1002/mrm.1910210107`](https://doi.org/10.1002/mrm.1910210107) |
| G03 | Gradient | 1992 Aug | Design and evaluation of shielded gradient coils | [`10.1002/mrm.1910260202`](https://doi.org/10.1002/mrm.1910260202) |
| G04 | Gradient | 1992 Jul | Minimum energy MRI gradient coils of general geometry | [`10.1088/0957-0233/3/7/007`](https://doi.org/10.1088/0957-0233/3/7/007) |
| G05 | Gradient | 1993 | Gradient coil design: A review of methods | [`10.1016/0730-725X(93)90209-V`](https://doi.org/10.1016/0730-725X%2893%2990209-V) |
| G06 | Gradient | 1994 | Biplanar gradient coil design by simulated annealing | [`10.1007/BF01705279`](https://doi.org/10.1007/BF01705279) |
| G07 | Gradient | 1995 | A design methodology for short, whole-body, shielded gradient coils for MRI | [`10.1016/0730-725X(95)00001-W`](https://doi.org/10.1016/0730-725X%2895%2900001-W) |
| G08 | Gradient | 1995 | Low inductance transverse gradient system of restricted length | [`10.1016/0730-725X(95)00002-X`](https://doi.org/10.1016/0730-725X%2895%2900002-X) |
| G09 | Gradient | 1997 Nov | Planar gradient coil design by scaling the spatial frequencies of minimum-inductance current density | [`10.1002/mrm.1910380525`](https://doi.org/10.1002/mrm.1910380525) |
| G10 | Gradient | 1997 | Design of a biplanar gradient coil using a genetic algorithm | [`10.1016/S0730-725X(96)00371-2`](https://doi.org/10.1016/S0730-725X%2896%2900371-2) |
| G11 | Gradient | 1998 Apr | Multilayer Gradient Coil Design | [`10.1006/jmre.1998.1369`](https://doi.org/10.1006/jmre.1998.1369) |
| G12 | Gradient | 1998 Feb | Constrained length minimum inductance gradient coil design | [`10.1002/mrm.1910390214`](https://doi.org/10.1002/mrm.1910390214) |
| G13 | Gradient | 1999 Jun | Design of biplanar gradient coils for magnetic resonance imaging of the human torso and limbs | [`10.1016/S0730-725X(99)00012-0`](https://doi.org/10.1016/S0730-725X%2899%2900012-0) |
| G14 | Gradient | 1999 Oct | Fast optimization of a biplanar gradient coil set | [`10.1006/jmre.1999.1832`](https://doi.org/10.1006/jmre.1999.1832) |
| G15 | Gradient | 2001 Jan | Application of the SUSHI method to the design of gradient coils | [`10.1002/1522-2594(200101)45:1<147::AID-MRM1019>3.0.CO;2-B`](https://doi.org/10.1002/1522-2594%28200101%2945:1%3C147::AID-MRM1019%3E3.0.CO%3B2-B) |
| G16 | Gradient | 2001 Mar | Stream function optimization for gradient coil design | [`10.1002/1522-2594(200103)45:3<505::AID-MRM1066>3.0.CO;2-H`](https://doi.org/10.1002/1522-2594%28200103%2945:3%3C505::AID-MRM1066%3E3.0.CO%3B2-H) |
| G17 | Gradient | 2003 Dec | Actively shielded multi-layer gradient coil designs with improved cooling properties | [`10.1016/j.jmr.2003.08.002`](https://doi.org/10.1016/j.jmr.2003.08.002) |
| G18 | Gradient | 2005 | A stream function method for gradient coil design | [`10.1002/cmr.b.20040`](https://doi.org/10.1002/cmr.b.20040) |
| G19 | Gradient | 2007 | Novel gradient coils designed using a boundary element method | [`10.1002/cmr.b.20091`](https://doi.org/10.1002/cmr.b.20091) |
| G20 | Gradient | 2009 May | 3D Gradient coil design – Toroidal surfaces | [`10.1016/j.jmr.2009.01.006`](https://doi.org/10.1016/j.jmr.2009.01.006) |
| G21 | Gradient | 2010 Oct | 3D gradient coil design for open MRI systems | [`10.1016/j.jmr.2010.08.017`](https://doi.org/10.1016/j.jmr.2010.08.017) |
| G22 | Gradient | 2010 | Theory of gradient coil design methods for magnetic resonance imaging | [`10.1002/cmr.a.20163`](https://doi.org/10.1002/cmr.a.20163) |
| G23 | Gradient | 2012 Sep | A finite difference method for the design of gradient coils in MRI—An initial framework | [`10.1109/TBME.2012.2188290`](https://doi.org/10.1109/TBME.2012.2188290) |
| G24 | Gradient | 2013 | Theoretical design of gradient coils with minimum power dissipation: accounting for the discretization of current density into coil windings | [`10.1016/j.jmr.2013.07.017`](https://doi.org/10.1016/j.jmr.2013.07.017) |
| G25 | Gradient / Shim | 2014 Jul | Convex optimisation of gradient and shim coil winding patterns | [`10.1016/j.jmr.2014.04.015`](https://doi.org/10.1016/j.jmr.2014.04.015) |
| G26 | Gradient | 2016 Aug | Asymmetric gradient coil design for use in a short, open bore magnetic resonance imaging scanner | [`10.1016/j.jmr.2016.06.015`](https://doi.org/10.1016/j.jmr.2016.06.015) |
| G27 | Gradient / Shim | 2018 Mar | Gradient and shim technologies for ultra high field MRI | [`10.1016/j.neuroimage.2016.11.033`](https://doi.org/10.1016/j.neuroimage.2016.11.033) |
| G28 | Gradient | 2021 Jul | Minimum electric-field gradient coil design: Theoretical limits and practical guidelines | [`10.1002/mrm.28681`](https://doi.org/10.1002/mrm.28681) |
| G29 | Gradient | 2021 | Methods: Of Stream Functions and Thin Wires: An Intuitive Approach to Gradient Coil Design | [`10.3389/fphy.2021.699468`](https://doi.org/10.3389/fphy.2021.699468) |
| G30 | Gradient | 2022 | A theoretical framework of gradient coil designed to mitigate eddy currents for a permanent magnet MRI system | [`10.3233/THC-THC228030`](https://doi.org/10.3233/THC-THC228030) |
| G31 | Gradient | 2023 | Gradient coil design with enhanced shielding constraint for a cryogen-free superconducting MRI system | [`10.1016/j.mrl.2023.09.001`](https://doi.org/10.1016/j.mrl.2023.09.001) |
| G32 | Gradient | 2023 Sep | A Stream Function Smoothing Method for the Design of MRI Gradient Coils on Non-Developable Surfaces | [`10.3390/s23187912`](https://doi.org/10.3390/s23187912) |
| G33 | Gradient | 2024 Jul | Designing gradient coils with the shape derivative and the closed B-spline curves | [`10.1016/j.mri.2024.03.042`](https://doi.org/10.1016/j.mri.2024.03.042) |
| G34 | Gradient | 2025 Jun | Design method of magnetic resonance biplanar gradient coil based on target field method and stream function | [`10.3389/fphy.2025.1579043`](https://doi.org/10.3389/fphy.2025.1579043) |
| G35 | Gradient | 2025 Oct | Gradient coil design for a 0.23 T NICU MRI system using an improved two-step Target-Field Method with enhanced linearity and compact design | [`10.1016/j.jmr.2025.107936`](https://doi.org/10.1016/j.jmr.2025.107936) |
| S01 | Shim | 1994 May | Accurate Shim-Coil Design and Magnet-Field Profiling by a Power-Minimization-Matrix Method | [`10.1006/jmra.1994.1082`](https://doi.org/10.1006/jmra.1994.1082) |
| S02 | Shim | 1995 Aug | Shim coils for NMR and MRI solenoid magnets | [`10.1088/0957-0233/6/8/005`](https://doi.org/10.1088/0957-0233/6/8/005) |
| S03 | Shim | 2001 Aug | Asymmetric zonal shim coils for magnetic resonance applications | [`10.1118/1.1388538`](https://doi.org/10.1118/1.1388538) |
| S04 | Shim | 2001 Dec | A novel target-field method for finite-length magnetic resonance shim coils: I. Zonal shims | [`10.1088/0022-3727/34/24/305`](https://doi.org/10.1088/0022-3727/34/24/305) |
| S05 | Shim | 2002 May | A novel target-field method for finite-length magnetic resonance shim coils: II. Tesseral shims | [`10.1088/0022-3727/35/9/303`](https://doi.org/10.1088/0022-3727/35/9/303) |
| S06 | Shim | 2002 | NMR shim coil design utilising a rapid spherical harmonic calculation method | [`10.1017/S1446181100012578`](https://doi.org/10.1017/S1446181100012578) |
| S07 | Shim | 2002 | Determining complicated winding patterns for shim coils using stream functions and the target-field method | [`10.1002/cmr.10000`](https://doi.org/10.1002/cmr.10000) |
| S08 | Shim | 2003 Jan | A novel target-field method for magnetic resonance shim coils: III. Shielded zonal and tesseral coils | [`10.1088/0022-3727/36/2/302`](https://doi.org/10.1088/0022-3727/36/2/302) |
| S09 | Shim | 2004 Sep | Shim design using a linear programming algorithm | [`10.1002/mrm.20176`](https://doi.org/10.1002/mrm.20176) |
| S10 | Shim | 2005 Feb | Mitigation of susceptibility-induced signal loss in neuroimaging using localized shim coils | [`10.1002/mrm.20365`](https://doi.org/10.1002/mrm.20365) |
| S11 | Shim | 2010 Apr | Quantitative Comparison of Minimum Inductance and Minimum Power Algorithms for the Design of Shim Coils for Small Animal Imaging | [`10.1002/cmr.b.20159`](https://doi.org/10.1002/cmr.b.20159) |
| S12 | Shim | 2010 Jan | Magnetic Field Homogenization of the Human Prefrontal Cortex with a Set of Localized Electrical Coils | [`10.1002/mrm.22164`](https://doi.org/10.1002/mrm.22164) |
| S13 | Shim / Encoding | 2010 Jun | Magnetic field modeling with a set of individual localized coils | [`10.1016/j.jmr.2010.03.008`](https://doi.org/10.1016/j.jmr.2010.03.008) |
| S14 | Shim | 2011 Sep | Multicoil shimming of the mouse brain | [`10.1002/mrm.22850`](https://doi.org/10.1002/mrm.22850) |
| S15 | Shim | 2011 Oct | Dynamic multi-coil shimming of the human brain at 7 T | [`10.1016/j.jmr.2011.07.005`](https://doi.org/10.1016/j.jmr.2011.07.005) |
| S16 | Shim | 2010 Jan | A novel approach to designing cylindrical-surface shim coils for a superconducting magnet of magnetic resonance imaging | [`10.1088/1674-1056/19/1/018701`](https://doi.org/10.1088/1674-1056/19/1/018701) |
| S17 | Shim | 2010 Feb | A novel target-field approach to design bi-planar shim coils for permanent-magnet MRI | [`10.1002/cmr.b.20153`](https://doi.org/10.1002/cmr.b.20153) |
| S18 | Shim | 2017 Jul | Theory and development of biplanar active shim coils for a permanent NMR analyzer | [`10.1371/journal.pone.0181552`](https://doi.org/10.1371/journal.pone.0181552) |
| S19 | Shim | 2018 Nov | Design of biplanar shim coils for ultra-low field MRI | [`10.3233/JAE-180025`](https://doi.org/10.3233/JAE-180025) |
| S20 | Shim | 2020 Apr | Design of a shim coil array matched to the human brain anatomy | [`10.1002/mrm.28016`](https://doi.org/10.1002/mrm.28016) |
| S21 | Shim | 2020 Apr | The orthogonal shim coil for 3-Tesla brain imaging | [`10.1002/mrm.28010`](https://doi.org/10.1002/mrm.28010) |
| S22 | Shim | 2021 Jan | A fieldmap-driven few-channel shim coil design for MRI of the human brain | [`10.1088/1361-6560/abc810`](https://doi.org/10.1088/1361-6560/abc810) |
| S23 | Gradient / Shim | 2022 Oct | Systematic dimensional analysis of the scaling relationship for gradient and shim coil design parameters | [`10.1002/mrm.29316`](https://doi.org/10.1002/mrm.29316) |
| S24 | Shim | 2022 | Improving brain B0 shimming using an easy and accessible multi-coil shim array at ultra-high field | [`10.1007/s10334-022-01014-6`](https://doi.org/10.1007/s10334-022-01014-6) |
| S25 | Shim / Encoding | 2023 Sep | Design and realization of a multi-coil array for B0 field control in a compact 1.5T head-only MRI scanner | [`10.1002/mrm.29692`](https://doi.org/10.1002/mrm.29692) |
| S26 | Shim | 2025 | Passive shimming method for permanent magnet MRI based on dynamic target magnetic field | [`10.1016/j.physo.2025.100296`](https://doi.org/10.1016/j.physo.2025.100296) |
| S27 | Shim | 2025 Dec | Passive shimming performance in 3 T MRI systems: Influence of shim parameters under varying magnet field distributions | [`10.1016/j.jmr.2025.107969`](https://doi.org/10.1016/j.jmr.2025.107969) |

## Gradient coil design papers

### G01. Gradient coil design using active magnetic screening

- **Area:** Gradient
- **Authors:** R. Bowtell; P. Mansfield
- **Venue / pages:** Magnetic Resonance in Medicine, 17(1), 15–19
- **Publication time:** 1991 Jan
- **DOI:** `10.1002/mrm.1910170105`
- **Links:** [DOI resolver](https://doi.org/10.1002/mrm.1910170105); [PubMed](https://pubmed.ncbi.nlm.nih.gov/2067392/)
- **Abstract (EN, paraphrased):** This paper formulates active magnetic screening for gradient coils. It describes how a second, actively driven coil can cancel external fringe fields so that switching gradients are decoupled from surrounding conducting structures, reducing eddy-current artifacts. The authors discuss design principles for screened coils and the construction issues that arise when the primary and shield systems must be co-optimized.
- **アブストラクト（日本語要約）:** 勾配コイルの能動磁気遮蔽を定式化した論文です。二次側の能動シールドコイルで外部漏洩磁場を打ち消し、周囲導体との結合と渦電流アーチファクトを低減する設計原理を述べています。一次コイルとシールドコイルを同時に成立させる際の設計上・製作上の問題も扱っています。

### G02. Coil optimization for MRI by conjugate gradient descent

- **Area:** Gradient
- **Authors:** E. C. Wong; A. Jesmanowicz; J. S. Hyde
- **Venue / pages:** Magnetic Resonance in Medicine, 21(1), 39–48
- **Publication time:** 1991 Sep
- **DOI:** `10.1002/mrm.1910210107`
- **Links:** [DOI resolver](https://doi.org/10.1002/mrm.1910210107); [PubMed](https://pubmed.ncbi.nlm.nih.gov/1943670/)
- **Abstract (EN, paraphrased):** The authors introduce a flexible iterative optimization framework for MRI coil design using discrete current elements and Biot–Savart field calculations. A user-defined error function over the region of interest is minimized by conjugate-gradient descent. The method can include field uniformity, efficiency, inductance, and power-related objectives without being restricted to simple cylindrical or planar geometries.
- **アブストラクト（日本語要約）:** 離散電流要素と Biot–Savart 則に基づき、MRI コイル設計を共役勾配法で最適化する枠組みを示した論文です。関心領域内の誤差関数を定義し、均一性、効率、インダクタンス、消費電力などを目的関数・制約として扱えます。単純な円筒面や平面に限定されない点が重要です。

### G03. Design and evaluation of shielded gradient coils

- **Area:** Gradient
- **Authors:** J. W. Carlson; K. A. Derby; K. C. Hawryszko; M. Weideman
- **Venue / pages:** Magnetic Resonance in Medicine, 26(2), 191–206
- **Publication time:** 1992 Aug
- **DOI:** `10.1002/mrm.1910260202`
- **Links:** [DOI resolver](https://doi.org/10.1002/mrm.1910260202)
- **Abstract (EN, paraphrased):** This work presents design and experimental evaluation methods for actively shielded gradient coils. It compares predicted and measured coil behavior and addresses the practical tradeoffs among gradient linearity, efficiency, inductance, and external-field suppression. The paper is one of the early post-1990 references that connects shielded-gradient theory with implementable MRI hardware.
- **アブストラクト（日本語要約）:** 能動シールド勾配コイルの設計と実験評価を扱った初期の重要論文です。勾配線形性、効率、インダクタンス、外部漏洩磁場抑制のトレードオフを、予測値と実測値の比較を通して検討しています。遮蔽勾配理論を実装可能な MRI ハードウェアへ結びつけた文献です。

### G04. Minimum energy MRI gradient coils of general geometry

- **Area:** Gradient
- **Authors:** S. Pissanetzky
- **Venue / pages:** Measurement Science and Technology, 3(7), 667–673
- **Publication time:** 1992 Jul
- **DOI:** `10.1088/0957-0233/3/7/007`
- **Links:** [DOI resolver](https://doi.org/10.1088/0957-0233/3/7/007); [ResearchGate record](https://www.researchgate.net/publication/230980431_Minimum_Energy_MRI_Gradient_Coils_of_General_Geometry)
- **Abstract (EN, paraphrased):** A general minimum-energy method is proposed for MRI gradient coils on arbitrary geometries. The formulation permits constraints such as finite cylinder length, finite planar support, current-free slots, eddy-current effects, and shielded or double-shielded structures. The optimization minimizes magnetic energy after these effects are included, yielding lower-energy and lower-inductance designs than comparable previous approaches.
- **アブストラクト（日本語要約）:** 任意形状の MRI 勾配コイルを最小エネルギーで設計する一般手法を提案しています。有限長円筒、有限平面、電流禁止領域、渦電流、シールドおよび二重シールドを制約として扱えます。これらを含めた後で磁気エネルギーを最小化し、従来設計より低エネルギー・低インダクタンスの勾配コイルを得ることを狙います。

### G05. Gradient coil design: A review of methods

- **Area:** Gradient
- **Authors:** R. Turner
- **Venue / pages:** Magnetic Resonance Imaging, 11(7), 903–920
- **Publication time:** 1993
- **DOI:** `10.1016/0730-725X(93)90209-V`
- **Links:** [DOI resolver](https://doi.org/10.1016/0730-725X%2893%2990209-V); [ScienceDirect](https://www.sciencedirect.com/science/article/pii/0730725X9390209V)
- **Abstract (EN, paraphrased):** This review organizes MRI gradient-coil design methods into discrete-wire and continuous-current-density approaches. It discusses field linearity, inductance, power dissipation, efficiency, low fringe fields, and active shielding. The paper is a useful map of the target-field, constrained-inductance, and constrained-power design literature up to the early 1990s.
- **アブストラクト（日本語要約）:** MRI 勾配コイル設計法を、離散ワイヤ法と連続電流密度法に整理した総説です。線形性、インダクタンス、消費電力、効率、漏洩磁場、能動遮蔽を比較しています。ターゲットフィールド法、制約付きインダクタンス最小化、制約付き電力最小化を理解するための基礎文献です。

### G06. Biplanar gradient coil design by simulated annealing

- **Area:** Gradient
- **Authors:** T. M. Peters; R. Bowtell
- **Venue / pages:** Magnetic Resonance Materials in Physics, Biology and Medicine, 2, 387–389
- **Publication time:** 1994
- **DOI:** `10.1007/BF01705279`
- **Links:** [DOI resolver](https://doi.org/10.1007/BF01705279); [Springer](https://link.springer.com/article/10.1007/BF01705279)
- **Abstract (EN, paraphrased):** The paper applies simulated annealing to the direct design of biplanar gradient coils for NMR microscopy. Instead of first solving for a continuous stream function, it optimizes wire positions directly with respect to homogeneity, efficiency, and power-related criteria. The study demonstrates the method for biplanar x- and z-gradient coils.
- **アブストラクト（日本語要約）:** NMR 顕微鏡用のバイプラナ勾配コイルを、シミュレーテッドアニーリングで直接設計する方法です。連続 stream function を先に求めるのではなく、ワイヤ位置を直接最適化し、均一性、効率、電力に関する指標を評価します。x 勾配および z 勾配のバイプラナコイル設計例を示しています。

### G07. A design methodology for short, whole-body, shielded gradient coils for MRI

- **Area:** Gradient
- **Authors:** S. Crozier; D. M. Doddrell
- **Venue / pages:** Magnetic Resonance Imaging, 13(4), 615–620
- **Publication time:** 1995
- **DOI:** `10.1016/0730-725X(95)00001-W`
- **Links:** [DOI resolver](https://doi.org/10.1016/0730-725X%2895%2900001-W); [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/0730725X9500001W)
- **Abstract (EN, paraphrased):** This paper uses real-space simulated annealing to design short whole-body shielded gradient coils. It emphasizes restricted-length systems, remote return paths, and the need to maintain a useful homogeneous gradient region while reducing external fields. The approach is relevant for compact or short-bore gradient systems.
- **アブストラクト（日本語要約）:** 短尺の全身用シールド勾配コイルを、実空間のシミュレーテッドアニーリングで設計する方法を示しています。制限長、リターンパス配置、有効な均一勾配領域、漏洩磁場低減の同時成立が主題です。短ボアやコンパクトな勾配系に関係する設計論です。

### G08. Low inductance transverse gradient system of restricted length

- **Area:** Gradient
- **Authors:** S. Crozier et al.
- **Venue / pages:** Magnetic Resonance Imaging, 13(4), 607–613
- **Publication time:** 1995
- **DOI:** `10.1016/0730-725X(95)00002-X`
- **Links:** [DOI resolver](https://doi.org/10.1016/0730-725X%2895%2900002-X); [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/0730725X9500002X)
- **Abstract (EN, paraphrased):** A restricted-length transverse gradient assembly is designed to provide a large usable region while keeping inductance low. The authors present a prototype and compare measured behavior with simulations. The design targets applications that require fast switching, such as head, animal, or microimaging MRI/NMR systems.
- **アブストラクト（日本語要約）:** 制限長の横方向勾配コイル系について、大きな使用可能領域と低インダクタンスを両立する設計を示しています。試作機を製作し、シミュレーションと測定を比較しています。高速スイッチングが必要な頭部、動物、NMR マイクロイメージング向けの設計として位置づけられます。

### G09. Planar gradient coil design by scaling the spatial frequencies of minimum-inductance current density

- **Area:** Gradient
- **Authors:** S. Y. Lee; B. S. Park; J. H. Yi; W. Yi
- **Venue / pages:** Magnetic Resonance in Medicine, 38(5), 858–861
- **Publication time:** 1997 Nov
- **DOI:** `10.1002/mrm.1910380525`
- **Links:** [DOI resolver](https://doi.org/10.1002/mrm.1910380525); [PubMed](https://pubmed.ncbi.nlm.nih.gov/9358463/); [Institutional record](https://khu.elsevierpure.com/en/publications/planar-gradient-coil-design-by-scaling-the-spatial-frequencies-of/)
- **Abstract (EN, paraphrased):** Minimum-inductance design can strongly reduce stored magnetic energy, but planar gradient coils obtained this way may have poor field linearity. This paper improves planar-coil linearity by scaling spatial frequencies in the current-density function. The result is a better figure of merit with only a small penalty in inductance.
- **アブストラクト（日本語要約）:** 最小インダクタンス設計は磁気エネルギーを下げられますが、平面勾配コイルでは線形性が悪化する場合があります。本論文は電流密度関数の空間周波数をスケーリングして線形性を改善します。わずかなインダクタンス増加と引き換えに、平面勾配コイルの性能指標を改善する方法です。

### G10. Design of a biplanar gradient coil using a genetic algorithm

- **Area:** Gradient
- **Authors:** B. J. Fisher et al.
- **Venue / pages:** Magnetic Resonance Imaging, 15(3), 369–376
- **Publication time:** 1997
- **DOI:** `10.1016/S0730-725X(96)00371-2`
- **Links:** [DOI resolver](https://doi.org/10.1016/S0730-725X%2896%2900371-2); [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0730725X96003712)
- **Abstract (EN, paraphrased):** The authors design a biplanar z-gradient coil by genetic algorithm optimization and compare its efficiency with a conventional Maxwell arrangement. The design is evaluated over a cuboid optimized region, and additional data are provided for transverse gradient coils. The paper illustrates how evolutionary optimization can handle unconventional biplanar gradient layouts.
- **アブストラクト（日本語要約）:** 遺伝的アルゴリズムでバイプラナ z 勾配コイルを設計し、Maxwell 型配置との効率比較を行っています。直方体の最適化領域で性能を評価し、横方向勾配セットの設計データも示しています。非標準的なバイプラナ配置を進化的最適化で扱う例です。

### G11. Multilayer Gradient Coil Design

- **Area:** Gradient
- **Authors:** R. Bowtell; P. Robyr
- **Venue / pages:** Journal of Magnetic Resonance, 131(2), 286–294
- **Publication time:** 1998 Apr
- **DOI:** `10.1006/jmre.1998.1369`
- **Links:** [DOI resolver](https://doi.org/10.1006/jmre.1998.1369); [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1090780798913696)
- **Abstract (EN, paraphrased):** The paper extends cylindrical gradient design to multiple radial layers. By allowing windings to spread over increasing radii, it improves the resistance–efficiency scaling that limits very strong single-layer gradients. A four-layer z-gradient coil is designed, built, and tested, demonstrating strong gradients with acceptable resistance and inductance.
- **アブストラクト（日本語要約）:** 円筒勾配コイルを多層巻線へ拡張する設計論文です。巻線を複数半径に分散させることで、単層コイルで問題となる抵抗と効率のスケーリングを改善します。4 層 z 勾配コイルを設計・製作・評価し、高強度勾配を現実的な抵抗とインダクタンスで実現できることを示しています。

### G12. Constrained length minimum inductance gradient coil design

- **Area:** Gradient
- **Authors:** B. A. Chronik; B. K. Rutt
- **Venue / pages:** Magnetic Resonance in Medicine, 39(2), 270–278
- **Publication time:** 1998 Feb
- **DOI:** `10.1002/mrm.1910390214`
- **Links:** [DOI resolver](https://doi.org/10.1002/mrm.1910390214); [PubMed](https://pubmed.ncbi.nlm.nih.gov/9469710/)
- **Abstract (EN, paraphrased):** This paper modifies the minimum-inductance target-field method so that explicit constraints can be placed on the final current density and on the position of the homogeneous ROI relative to the winding surface. It gives implementation equations and examples for central and edge-of-cylinder regions. The method is useful for short or specialized magnet geometries.
- **アブストラクト（日本語要約）:** 最小インダクタンス・ターゲットフィールド法を拡張し、最終的な電流密度や、巻線面に対する均一 ROI の位置に制約を課せるようにしています。実装に必要な式と、中央 ROI および円筒端部 ROI の設計例を示します。短尺磁石や特殊形状磁石向けの勾配設計に有用です。

### G13. Design of biplanar gradient coils for magnetic resonance imaging of the human torso and limbs

- **Area:** Gradient
- **Authors:** G. B. Wills et al.
- **Venue / pages:** Magnetic Resonance Imaging, 17(5), 739–754
- **Publication time:** 1999 Jun
- **DOI:** `10.1016/S0730-725X(99)00012-0`
- **Links:** [DOI resolver](https://doi.org/10.1016/S0730-725X%2899%2900012-0); [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0730725X99000120)
- **Abstract (EN, paraphrased):** A biplanar gradient design method is presented for imaging body parts that benefit from open access. The method superposes Biot–Savart fields from individual current elements and uses a genetic algorithm to explore coil shapes. A two-axis biplanar gradient set for torso and limb imaging is reported.
- **アブストラクト（日本語要約）:** 開放アクセスが有利な体幹・四肢 MRI 用のバイプラナ勾配コイル設計を扱います。個別電流要素の Biot–Savart 磁場を重ね合わせ、遺伝的アルゴリズムでコイル形状を探索します。体幹・四肢向けの 2 軸バイプラナ勾配セットを示しています。

### G14. Fast optimization of a biplanar gradient coil set

- **Area:** Gradient
- **Authors:** D. Tomasi; E. C. Caparelli; H. Panepucci; B. Foerster
- **Venue / pages:** Journal of Magnetic Resonance, 140(2), 325–339
- **Publication time:** 1999 Oct
- **DOI:** `10.1006/jmre.1999.1832`
- **Links:** [DOI resolver](https://doi.org/10.1006/jmre.1999.1832); [PubMed](https://pubmed.ncbi.nlm.nih.gov/10497040/); [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1090780799918323)
- **Abstract (EN, paraphrased):** The authors accelerate simulated-annealing optimization for shielded biplanar gradient coils by using target-field-derived shielding conditions and analytic field expressions for simple geometries. Efficiency, inductance, homogeneity, and shielding are studied as functions of wire number. A prototype validates the calculated coil performance.
- **アブストラクト（日本語要約）:** ターゲットフィールド法から得たシールド条件と単純形状の解析的磁場式を利用し、バイプラナ・シールド勾配コイルのシミュレーテッドアニーリングを高速化しています。ワイヤ本数に対する効率、インダクタンス、均一性、遮蔽性能を評価し、試作機で理論値との整合を確認しています。

### G15. Application of the SUSHI method to the design of gradient coils

- **Area:** Gradient
- **Authors:** S. M. Shvartsman et al.
- **Venue / pages:** Magnetic Resonance in Medicine, 45(1), 147–155
- **Publication time:** 2001 Jan
- **DOI:** `10.1002/1522-2594(200101)45:1<147::AID-MRM1019>3.0.CO;2-B`
- **Links:** [DOI resolver](https://doi.org/10.1002/1522-2594%28200101%2945:1%3C147::AID-MRM1019%3E3.0.CO%3B2-B); [PubMed](https://pubmed.ncbi.nlm.nih.gov/11146496/)
- **Abstract (EN, paraphrased):** The paper applies the SUSHI method, based on supershielding current conditions, to cylindrical gradient-coil design. The goal is stronger suppression of fields outside a finite-length active shield while preserving the target field in the imaging volume. The method improves shielding for short axial and transverse gradients, at the cost of higher current peaks and stored energy.
- **アブストラクト（日本語要約）:** 超遮蔽条件に基づく SUSHI 法を円筒勾配コイル設計へ適用した論文です。有限長の能動シールド外側の磁場を強く抑えつつ、撮像領域内のターゲット勾配場を保つことを目指します。短尺の軸方向・横方向勾配で遮蔽性能を改善しますが、電流ピークや磁気エネルギーが増えるトレードオフがあります。

### G16. Stream function optimization for gradient coil design

- **Area:** Gradient
- **Authors:** D. Tomasi
- **Venue / pages:** Magnetic Resonance in Medicine, 45(3), 505–512
- **Publication time:** 2001 Mar
- **DOI:** `10.1002/1522-2594(200103)45:3<505::AID-MRM1066>3.0.CO;2-H`
- **Links:** [DOI resolver](https://doi.org/10.1002/1522-2594%28200103%2945:3%3C505::AID-MRM1066%3E3.0.CO%3B2-H); [PubMed](https://pubmed.ncbi.nlm.nih.gov/11241709/)
- **Abstract (EN, paraphrased):** This work parameterizes cylindrical gradient-coil current density by stream functions and optimizes them, combining target-field ideas with simulated annealing. It targets short self-shielded cylindrical gradients and compares performance with conventional target-field designs. The method can enlarge the homogeneous volume and reduce inductance for selected cases.
- **アブストラクト（日本語要約）:** 円筒勾配コイルの電流密度を stream function でパラメータ化し、ターゲットフィールド法とシミュレーテッドアニーリングを組み合わせて最適化します。短尺自己シールド円筒勾配を対象とし、従来のターゲットフィールド設計と比較しています。条件によっては均一体積の拡大とインダクタンス低減が得られます。

### G17. Actively shielded multi-layer gradient coil designs with improved cooling properties

- **Area:** Gradient
- **Authors:** M. Poole; R. Bowtell et al.
- **Venue / pages:** Journal of Magnetic Resonance, 165(2), 196–207
- **Publication time:** 2003 Dec
- **DOI:** `10.1016/j.jmr.2003.08.002`
- **Links:** [DOI resolver](https://doi.org/10.1016/j.jmr.2003.08.002); [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1090780703002817)
- **Abstract (EN, paraphrased):** The multilayer gradient concept is extended to actively shielded coils with improved cooling and resistance behavior. The design addresses the strong-gradient problem in small-bore MRI, where single-layer coils become resistance-limited. The work links electromagnetic optimization with practical thermal and winding constraints.
- **アブストラクト（日本語要約）:** 多層勾配コイル設計を、冷却性を改善した能動シールド構造へ拡張しています。小口径 MRI では単層コイルが抵抗で制約されるため、多層化とシールド化を組み合わせて強い勾配を実現する設計です。電磁場最適化と熱・巻線制約を結びつけています。

### G18. A stream function method for gradient coil design

- **Area:** Gradient
- **Authors:** R. A. Lemdiasov; R. Ludwig
- **Venue / pages:** Concepts in Magnetic Resonance Part B, 26B(1), 67–80
- **Publication time:** 2005
- **DOI:** `10.1002/cmr.b.20040`
- **Links:** [DOI resolver](https://doi.org/10.1002/cmr.b.20040)
- **Abstract (EN, paraphrased):** This paper formulates gradient-coil design as an inverse problem for a surface stream function. A Biot–Savart based cost function is defined on an arbitrary current-carrying surface, and suitable weighting and linearization reduce the problem to a matrix equation. The stream-function solution is then converted into discrete winding paths.
- **アブストラクト（日本語要約）:** 任意の電流担持面上の stream function を未知量とする逆問題として、勾配コイル設計を定式化しています。Biot–Savart 則に基づくコスト関数を重み付け・線形化し、行列方程式として解きます。得られた stream function から離散巻線パターンを抽出します。

### G19. Novel gradient coils designed using a boundary element method

- **Area:** Gradient
- **Authors:** M. Poole; R. Bowtell
- **Venue / pages:** Concepts in Magnetic Resonance Part B, 31B(3), 162–175
- **Publication time:** 2007
- **DOI:** `10.1002/cmr.b.20091`
- **Links:** [DOI resolver](https://doi.org/10.1002/cmr.b.20091)
- **Abstract (EN, paraphrased):** The authors use a boundary element method to design gradient coils on arbitrarily shaped surfaces. The surface is meshed, current density is represented by stream functions, and the optimizer can target Maxwell-consistent field variations while including resistance, inductance, torque, or shielding-related terms. Examples include asymmetric and shielded gradient surfaces.
- **アブストラクト（日本語要約）:** 境界要素法を用いて、任意形状面上の勾配コイルを設計する方法です。表面メッシュ上で stream function により電流密度を表し、Maxwell 方程式と整合する目標場を生成します。抵抗、インダクタンス、トルク、遮蔽に関する項を含められ、非対称・シールド付き勾配面の設計例が示されます。

### G20. 3D Gradient coil design – Toroidal surfaces

- **Area:** Gradient
- **Authors:** P. T. While; L. K. Forbes; S. Crozier
- **Venue / pages:** Journal of Magnetic Resonance, 198(1), 31–40
- **Publication time:** 2009 May
- **DOI:** `10.1016/j.jmr.2009.01.006`
- **Links:** [DOI resolver](https://doi.org/10.1016/j.jmr.2009.01.006); [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1090780709000123)
- **Abstract (EN, paraphrased):** This paper develops an inverse design method for transverse gradient coils on toroidal surfaces. The optimization combines field-error control with regularization terms related to power and practical winding behavior. It explores unshielded and shielded designs for whole-body and head-scale MRI.
- **アブストラクト（日本語要約）:** トロイダル面上の横方向勾配コイルを逆問題として設計する方法です。磁場誤差と、電力・巻線実装性に関する正則化項を組み合わせて最適化します。全身用および頭部用の非シールド・シールド付き設計を扱っています。

### G21. 3D gradient coil design for open MRI systems

- **Area:** Gradient
- **Authors:** P. T. While; L. K. Forbes; S. Crozier
- **Venue / pages:** Journal of Magnetic Resonance, 207(1), 124–133
- **Publication time:** 2010 Oct
- **DOI:** `10.1016/j.jmr.2010.08.017`
- **Links:** [DOI resolver](https://doi.org/10.1016/j.jmr.2010.08.017); [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1090780710002739)
- **Abstract (EN, paraphrased):** An analytic inverse method is presented for obtaining three-dimensional gradient coil geometries appropriate for open MRI. The design uses Fourier-series representations and Tikhonov regularization, with objectives such as field accuracy, power minimization, and optional shielding. Streamlines of the optimized current density provide implementable winding paths.
- **アブストラクト（日本語要約）:** 開放型 MRI 用の三次元勾配コイル形状を求める解析的逆設計法です。Fourier 級数表現と Tikhonov 正則化を用い、磁場精度、電力最小化、任意の遮蔽条件を扱います。最適化された電流密度の流線から実装可能な巻線経路を得ます。

### G22. Theory of gradient coil design methods for magnetic resonance imaging

- **Area:** Gradient
- **Authors:** S. S. Hidalgo-Tobon
- **Venue / pages:** Concepts in Magnetic Resonance Part A, 36A(4), 223–242
- **Publication time:** 2010
- **DOI:** `10.1002/cmr.a.20163`
- **Links:** [DOI resolver](https://doi.org/10.1002/cmr.a.20163)
- **Abstract (EN, paraphrased):** This review explains the theoretical basis of MRI gradient-coil design methods. It emphasizes the competing requirements of efficiency, slew rate, low inductance, linearity, low power, low eddy-current interaction, and mechanical/acoustic constraints. It is a compact entry point to the two decades of gradient design literature preceding 2010.
- **アブストラクト（日本語要約）:** MRI 勾配コイル設計法の理論的基礎を解説する総説です。効率、スルーレート、低インダクタンス、線形性、低消費電力、渦電流との低結合、機械・音響制約など、互いに競合する要求を整理しています。2010 年以前の勾配設計文献への導入として有用です。

### G23. A finite difference method for the design of gradient coils in MRI—An initial framework

- **Area:** Gradient
- **Authors:** X. Zhu; L. Xia; W. Liu; S. Crozier
- **Venue / pages:** IEEE Transactions on Biomedical Engineering, 59(9), 2412–2421
- **Publication time:** 2012 Sep
- **DOI:** `10.1109/TBME.2012.2188290`
- **Links:** [DOI resolver](https://doi.org/10.1109/TBME.2012.2188290); [PubMed](https://pubmed.ncbi.nlm.nih.gov/22345557/)
- **Abstract (EN, paraphrased):** The paper introduces a finite-difference framework for representing continuous current density in MRI gradient-coil design. A stream function is used to extract winding patterns after solving a regularized linear system. The framework supports biplanar, cylindrical, and less conventional coil geometries in a unified discretized formulation.
- **アブストラクト（日本語要約）:** 有限差分法により、MRI 勾配コイル設計における連続電流密度を表現する枠組みを導入しています。正則化線形方程式を解いた後、stream function から巻線パターンを抽出します。バイプラナ、円筒、非標準形状を統一的な離散化形式で扱えます。

### G24. Theoretical design of gradient coils with minimum power dissipation: accounting for the discretization of current density into coil windings

- **Area:** Gradient
- **Authors:** P. T. While; J. G. Korvink; N. J. Shah; M. S. Poole
- **Venue / pages:** Journal of Magnetic Resonance, 235, 85–94
- **Publication time:** 2013
- **DOI:** `10.1016/j.jmr.2013.07.017`
- **Links:** [DOI resolver](https://doi.org/10.1016/j.jmr.2013.07.017)
- **Abstract (EN, paraphrased):** This work studies the gap between continuous-current-density optimization and the discrete winding patterns actually manufactured. It focuses on minimum-power gradient-coil design while accounting for the effect of contouring the current density into finite wire paths. The paper is relevant when stream-function designs must be converted into practical windings without losing predicted performance.
- **アブストラクト（日本語要約）:** 連続電流密度として最適化された設計と、実際に製作される離散巻線との間の差を扱う論文です。最小消費電力の勾配コイル設計において、stream function の等高線化が性能に与える影響を考慮します。連続解を実用巻線へ変換する際に重要です。

### G25. Convex optimisation of gradient and shim coil winding patterns

- **Area:** Gradient / Shim
- **Authors:** M. S. Poole et al.
- **Venue / pages:** Journal of Magnetic Resonance, 244, 36–45
- **Publication time:** 2014 Jul
- **DOI:** `10.1016/j.jmr.2014.04.015`
- **Links:** [DOI resolver](https://doi.org/10.1016/j.jmr.2014.04.015); [PubMed](https://pubmed.ncbi.nlm.nih.gov/24880337/)
- **Abstract (EN, paraphrased):** This paper combines boundary-element coil modeling with convex optimization to design both gradient and shim winding patterns. It compares cost functions and constraints, including lp-norm style regularization. Sparse or evenly distributed wire patterns can be encouraged, making the method useful when wire width, manufacturability, or local density constraints matter.
- **アブストラクト（日本語要約）:** 境界要素法によるコイルモデルと凸最適化を組み合わせ、勾配コイルとシムコイルの巻線パターンを設計します。lp ノルム型の正則化など、目的関数と制約を比較します。疎な巻線や均一な巻線分布を誘導でき、ワイヤ幅、製作性、局所密度制約が重要な場合に有用です。

### G26. Asymmetric gradient coil design for use in a short, open bore magnetic resonance imaging scanner

- **Area:** Gradient
- **Authors:** W. Wang et al.
- **Venue / pages:** Journal of Magnetic Resonance, 269, 203–212
- **Publication time:** 2016 Aug
- **DOI:** `10.1016/j.jmr.2016.06.015`
- **Links:** [DOI resolver](https://doi.org/10.1016/j.jmr.2016.06.015); [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S109078071630112X)
- **Abstract (EN, paraphrased):** The paper addresses the reduced imaging volume of short-bore scanners by designing asymmetric gradients that place a full-size imaging region closer to the coil end. The optimized, connected coil layouts loosen geometric restrictions and improve electromagnetic performance for short open-bore MRI. The work is relevant to access-constrained magnet architectures.
- **アブストラクト（日本語要約）:** 短ボア MRI で撮像可能領域が制限される問題に対し、コイル端部近傍に十分な撮像領域を置ける非対称勾配設計を提案しています。接続された最適化巻線により、配置制約を緩和し電磁性能を改善します。アクセス制約の強い磁石構成に関係します。

### G27. Gradient and shim technologies for ultra high field MRI

- **Area:** Gradient / Shim
- **Authors:** S. A. M. Winkler et al.
- **Venue / pages:** NeuroImage, 168, 59–70
- **Publication time:** 2018 Mar
- **DOI:** `10.1016/j.neuroimage.2016.11.033`
- **Links:** [DOI resolver](https://doi.org/10.1016/j.neuroimage.2016.11.033); [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1053811916306502)
- **Abstract (EN, paraphrased):** This review covers gradient and shim technology for ultra-high-field MRI. It discusses modeling, construction, Lorentz forces, vibration and acoustic noise, eddy currents, peripheral nerve stimulation, and insert gradient concepts. It is a useful cross-reference because high-field systems make both gradient performance and B0 homogenization more demanding.
- **アブストラクト（日本語要約）:** 超高磁場 MRI における勾配・シム技術の総説です。モデリング、製作、Lorentz 力、振動・騒音、渦電流、末梢神経刺激、挿入型勾配コイルを扱います。高磁場では勾配性能と B0 均一化の要求が厳しくなるため、両者を同時に俯瞰できる文献です。

### G28. Minimum electric-field gradient coil design: Theoretical limits and practical guidelines

- **Area:** Gradient
- **Authors:** P. B. Roemer; B. K. Rutt
- **Venue / pages:** Magnetic Resonance in Medicine, 86(1), 569–580
- **Publication time:** 2021 Jul
- **DOI:** `10.1002/mrm.28681`
- **Links:** [DOI resolver](https://doi.org/10.1002/mrm.28681); [PubMed](https://pubmed.ncbi.nlm.nih.gov/33604991/)
- **Abstract (EN, paraphrased):** This paper incorporates induced electric-field calculations directly into gradient-coil design. The design objective constrains peak electric field while preserving imaging-field constraints, allowing exploration of theoretical limits related to peripheral nerve stimulation. Asymmetric winding solutions can reduce E-field exposure for a given gradient requirement.
- **アブストラクト（日本語要約）:** 誘導電場計算を勾配コイル設計に直接組み込んだ論文です。撮像に必要な勾配場制約を維持しながらピーク電場を制約し、末梢神経刺激に関係する理論限界を探索します。非対称巻線により、同じ勾配要求に対して電場曝露を下げられる可能性を示しています。

### G29. Methods: Of Stream Functions and Thin Wires: An Intuitive Approach to Gradient Coil Design

- **Area:** Gradient
- **Authors:** S. Littin et al.
- **Venue / pages:** Frontiers in Physics, 9, 699468
- **Publication time:** 2021
- **DOI:** `10.3389/fphy.2021.699468`
- **Links:** [DOI resolver](https://doi.org/10.3389/fphy.2021.699468); [Frontiers](https://www.frontiersin.org/articles/10.3389/fphy.2021.699468/full)
- **Abstract (EN, paraphrased):** This methods paper provides an intuitive and open-source-oriented route from surface current density to stream functions and thin-wire gradient windings. It demonstrates how inverse coil design can be implemented on simple surfaces and several topologies. The value is mainly pedagogical and reproducibility-oriented for stream-function based gradient design.
- **アブストラクト（日本語要約）:** 表面電流密度から stream function、さらに細線巻線へ変換する流れを、直感的かつオープンソース志向で説明した方法論文です。単純面や複数の表面トポロジーで逆問題型コイル設計を実装する例を示します。stream function 型勾配設計の教育・再現性に価値があります。

### G30. A theoretical framework of gradient coil designed to mitigate eddy currents for a permanent magnet MRI system

- **Area:** Gradient
- **Authors:** P. Zhang; W. Wang; Y. Shi
- **Venue / pages:** Technology and Health Care, 30(1_suppl)
- **Publication time:** 2022
- **DOI:** `10.3233/THC-THC228030`
- **Links:** [DOI resolver](https://doi.org/10.3233/THC-THC228030); [SAGE page](https://journals.sagepub.com/doi/10.3233/THC-THC228030)
- **Abstract (EN, paraphrased):** The authors develop a planar-gradient design framework for permanent-magnet MRI systems where active shielding may be geometrically difficult. A mirror-image magnetostatic model and finite-difference stream-function formulation are used to reduce eddy currents in conductive plates and pole pieces. The method aims at minimum power dissipation and magnetic energy under practical spacing constraints.
- **アブストラクト（日本語要約）:** 能動シールドを配置しにくい永久磁石 MRI 向けに、平面勾配コイルの渦電流低減設計枠組みを提案しています。磁気静的ミラーイメージモデルと有限差分 stream function を用い、導体板やポールピースの渦電流を抑えます。実装空間制約下で、消費電力と磁気エネルギーを小さくする設計です。

### G31. Gradient coil design with enhanced shielding constraint for a cryogen-free superconducting MRI system

- **Area:** Gradient
- **Authors:** W. Wang et al.
- **Venue / pages:** Magnetic Resonance Letters, 4(1), 100086
- **Publication time:** 2023
- **DOI:** `10.1016/j.mrl.2023.09.001`
- **Links:** [DOI resolver](https://doi.org/10.1016/j.mrl.2023.09.001); [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2772528623000462)
- **Abstract (EN, paraphrased):** This paper proposes enhanced shielding constraints for gradient coils in cryogen-free superconducting MRI. Regionalized stray-field constraints are added so the optimized coil suppresses leakage in particularly sensitive regions without a large increase in winding complexity. The design is validated through a built gradient assembly and imaging assessment.
- **アブストラクト（日本語要約）:** 無冷媒超電導 MRI 用の勾配コイルに、強化された遮蔽制約を導入する研究です。敏感な領域ごとに漏洩磁場制約を設定し、巻線複雑性を大きく増やさずに外部磁場を低減します。勾配アセンブリの製作と画像評価により設計を検証しています。

### G32. A Stream Function Smoothing Method for the Design of MRI Gradient Coils on Non-Developable Surfaces

- **Area:** Gradient
- **Authors:** H. Yang; X. Ren; S. Zuo; W. Liu
- **Venue / pages:** Sensors, 23(18), 7912
- **Publication time:** 2023 Sep
- **DOI:** `10.3390/s23187912`
- **Links:** [DOI resolver](https://doi.org/10.3390/s23187912); [MDPI](https://www.mdpi.com/1424-8220/23/18/7912)
- **Abstract (EN, paraphrased):** The paper addresses winding extraction on non-developable surfaces, where raw stream-function contours can be difficult to manufacture. A smoothing operator based on the Laplace–Beltrami framework is applied to implicit stream functions before contour extraction. The method balances field accuracy, power, wire spacing, and wire curvature on complex coil surfaces.
- **アブストラクト（日本語要約）:** 非可展面上の勾配コイルで、stream function の等高線が製作困難になりやすい問題を扱います。Laplace–Beltrami 型の平滑化作用素を stream function に適用してから等高線を抽出します。複雑曲面で、磁場精度、電力、ワイヤ間隔、曲率を同時に改善することを狙います。

### G33. Designing gradient coils with the shape derivative and the closed B-spline curves

- **Area:** Gradient
- **Authors:** T. Takahashi
- **Venue / pages:** Magnetic Resonance Imaging, 110, 112–127
- **Publication time:** 2024 Jul
- **DOI:** `10.1016/j.mri.2024.03.042`
- **Links:** [DOI resolver](https://doi.org/10.1016/j.mri.2024.03.042); [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0730725X24000422)
- **Abstract (EN, paraphrased):** This paper treats discrete gradient-coil design as a shape-optimization problem. The derivative of the Bz gradient with respect to coil shape is derived, and closed B-spline curves are used so their control points become nonlinear-programming variables. The approach offers a gradient-based alternative to purely contour-based or stochastic winding optimization.
- **アブストラクト（日本語要約）:** 離散勾配コイル設計を形状最適化問題として扱う論文です。コイル形状に対する Bz 勾配の形状微分を導出し、閉 B-spline 曲線の制御点を非線形計画問題の設計変数とします。等高線抽出や確率的探索に対する、勾配ベースの代替アプローチです。

### G34. Design method of magnetic resonance biplanar gradient coil based on target field method and stream function

- **Area:** Gradient
- **Authors:** Q. Huang et al.
- **Venue / pages:** Frontiers in Physics, 13, 1579043
- **Publication time:** 2025 Jun
- **DOI:** `10.3389/fphy.2025.1579043`
- **Links:** [DOI resolver](https://doi.org/10.3389/fphy.2025.1579043); [Frontiers](https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2025.1579043/full)
- **Abstract (EN, paraphrased):** The authors combine a target-field point method with stream-function theory to design biplanar gradient coils. Inverse simulation is used to obtain a winding distribution, followed by solid modeling and orthogonal analysis. The design is iteratively adjusted for linearity, efficiency, and uniformity within the desired spherical volume.
- **アブストラクト（日本語要約）:** ターゲットフィールド点法と stream function 理論を組み合わせ、バイプラナ勾配コイルを設計しています。逆解析で巻線分布を求めた後、ソリッドモデル化と直交分析を行います。DSV 内の線形性、効率、均一性を反復的に改善する設計手順です。

### G35. Gradient coil design for a 0.23 T NICU MRI system using an improved two-step Target-Field Method with enhanced linearity and compact design

- **Area:** Gradient
- **Authors:** Jinhao Liu; Miutian Wang; Wenchen Wang; Yaohui Wang; Weimin Wang; Feng Liu
- **Venue / pages:** Journal of Magnetic Resonance, 379, 107936
- **Publication time:** 2025 Oct
- **DOI:** `10.1016/j.jmr.2025.107936`
- **Links:** [DOI resolver](https://doi.org/10.1016/j.jmr.2025.107936); [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1090780725001089)
- **Abstract (EN, paraphrased):** This paper targets a compact neonatal intensive care unit MRI system at 0.23 T. It uses a two-step target-field method: a Tikhonov-regularized linear solve followed by nonlinear constrained optimization. The goal is to improve absolute and relative gradient linearity while accommodating compact geometry and finite gradient thickness.
- **アブストラクト（日本語要約）:** 0.23 T の NICU 向けコンパクト MRI を対象とする勾配コイル設計です。Tikhonov 正則化を伴う線形解法と、その後の制約付き非線形最適化からなる二段階ターゲットフィールド法を用います。小型形状と有限厚みを考慮しつつ、絶対・相対線形性を改善することを目指します。

## Shim coil and B0 field-control design papers

### S01. Accurate Shim-Coil Design and Magnet-Field Profiling by a Power-Minimization-Matrix Method

- **Area:** Shim
- **Authors:** D. I. Hoult; D. Deslauriers
- **Venue / pages:** Journal of Magnetic Resonance, Series A, 108(1), 9–20
- **Publication time:** 1994 May
- **DOI:** `10.1006/jmra.1994.1082`
- **Links:** [DOI resolver](https://doi.org/10.1006/jmra.1994.1082); [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1064185884710820)
- **Abstract (EN, paraphrased):** This paper presents a power-minimization matrix method for designing shim coils that correct measured magnet inhomogeneity. The method uses basis functions and matrix optimization to obtain a current distribution that cancels unwanted field terms with minimum power. It also links shim-coil design with magnet-field profiling and practical correction strategies.
- **アブストラクト（日本語要約）:** 測定された磁石不均一を補正するシムコイルを、最小電力の行列法で設計する論文です。基底関数と行列最適化を用い、不要な磁場成分を最小電力で打ち消す電流分布を求めます。シムコイル設計と磁場プロファイリングを結びつける実用的な補正法です。

### S02. Shim coils for NMR and MRI solenoid magnets

- **Area:** Shim
- **Authors:** P. Konzbul; K. Švéda
- **Venue / pages:** Measurement Science and Technology, 6(8), 1116–1123
- **Publication time:** 1995 Aug
- **DOI:** `10.1088/0957-0233/6/8/005`
- **Links:** [DOI resolver](https://doi.org/10.1088/0957-0233/6/8/005)
- **Abstract (EN, paraphrased):** This paper treats shim-coil design for solenoidal NMR and MRI magnets. It belongs to the classical line of work in which specific harmonic correction fields are generated by tailored current distributions on cylindrical surfaces. It is useful for understanding the relation between conventional solenoid-magnet shims and later MRI-specific target-field methods.
- **アブストラクト（日本語要約）:** NMR および MRI のソレノイド磁石向けシムコイル設計を扱う論文です。円筒面上の電流分布で特定の調和補正場を生成する古典的な設計系譜に属します。従来のソレノイド磁石用シムと、後の MRI 向けターゲットフィールド法との接続を理解するのに有用です。

### S03. Asymmetric zonal shim coils for magnetic resonance applications

- **Area:** Shim
- **Authors:** L. K. Forbes; S. Crozier
- **Venue / pages:** Medical Physics, 28(8), 1644–1651
- **Publication time:** 2001 Aug
- **DOI:** `10.1118/1.1388538`
- **Links:** [DOI resolver](https://doi.org/10.1118/1.1388538); [PubMed](https://pubmed.ncbi.nlm.nih.gov/11548933/)
- **Abstract (EN, paraphrased):** The authors give a systematic Fourier-series design method for asymmetric zonal shim coils on finite cylinders. A desired field is specified over a nonsymmetric axial portion of the coil, and the current density and winding patterns follow from calculated Fourier coefficients. The method supports head-only and asymmetric magnet systems.
- **アブストラクト（日本語要約）:** 有限円筒上の非対称 zonal シムコイルを、Fourier 級数により系統的に設計する方法です。コイル長の非対称な軸方向領域に目標場を指定し、Fourier 係数から電流密度と巻線パターンを得ます。頭部専用磁石や非対称磁石系に適用しやすい設計です。

### S04. A novel target-field method for finite-length magnetic resonance shim coils: I. Zonal shims

- **Area:** Shim
- **Authors:** L. K. Forbes; S. Crozier
- **Venue / pages:** Journal of Physics D: Applied Physics, 34(24), 3447–3455
- **Publication time:** 2001 Dec
- **DOI:** `10.1088/0022-3727/34/24/305`
- **Links:** [DOI resolver](https://doi.org/10.1088/0022-3727/34/24/305); [Eurekamag record](https://eurekamag.com/research/098/987/098987476.php)
- **Abstract (EN, paraphrased):** This paper introduces a target-field method for genuinely finite-length magnetic resonance shim and gradient coils. A cylindrical target region can be placed asymmetrically inside a finite coil, and a desired field is specified on its surface. A regularized minimization produces the surface current density for zonal fields such as linear, quadratic, and cubic components.
- **アブストラクト（日本語要約）:** 有限長の磁気共鳴シム・勾配コイルを設計するターゲットフィールド法を導入しています。有限長コイル内の任意位置に円筒状ターゲット領域を置き、その表面上に目標磁場を指定します。正則化付き最小化により、線形、二次、三次などの zonal 成分を生成する表面電流密度を求めます。

### S05. A novel target-field method for finite-length magnetic resonance shim coils: II. Tesseral shims

- **Area:** Shim
- **Authors:** L. K. Forbes; S. Crozier
- **Venue / pages:** Journal of Physics D: Applied Physics, 35(9), 839–849
- **Publication time:** 2002 May
- **DOI:** `10.1088/0022-3727/35/9/303`
- **Links:** [DOI resolver](https://doi.org/10.1088/0022-3727/35/9/303)
- **Abstract (EN, paraphrased):** The second paper extends the finite-length target-field method to tesseral shim fields. It avoids assuming an ideal infinitely long geometry and allows asymmetric target regions and fields specified on more than one radius. The method provides winding patterns for higher-order tesseral shim terms in realistic finite coils.
- **アブストラクト（日本語要約）:** 有限長ターゲットフィールド法を tesseral シム場へ拡張した論文です。無限長コイル近似に依存せず、非対称ターゲット領域や複数半径上で指定した目標場を扱えます。現実的な有限長コイルで高次 tesseral シム項の巻線パターンを得る方法です。

### S06. NMR shim coil design utilising a rapid spherical harmonic calculation method

- **Area:** Shim
- **Authors:** C. J. Snape-Jenkinson; S. Crozier; L. K. Forbes
- **Venue / pages:** The ANZIAM Journal, 43(3), 375–386
- **Publication time:** 2002
- **DOI:** `10.1017/S1446181100012578`
- **Links:** [DOI resolver](https://doi.org/10.1017/S1446181100012578); [Cambridge Core](https://www.cambridge.org/core/journals/anziam-journal/article/nmr-shim-coil-design-utilising-a-rapid-spherical-harmonic-calculation-method/7305DDB8F04A05445E7C034332076475)
- **Abstract (EN, paraphrased):** The paper uses a rapid spherical-harmonic calculation method to design shim coils from circular-arc conductors. Simulated annealing is used to locate current-carrying arcs so that undesired harmonic terms are minimized while the desired shim term remains. The method is flexible for both zonal and tesseral fields.
- **アブストラクト（日本語要約）:** 円弧状導体からなるシムコイルを、高速な球面調和関数計算法で設計します。シミュレーテッドアニーリングにより電流円弧の位置を決め、目的のシム項を保ちながら不要な調和成分を小さくします。zonal と tesseral の両方に対応できる柔軟な方法です。

### S07. Determining complicated winding patterns for shim coils using stream functions and the target-field method

- **Area:** Shim
- **Authors:** M. A. Brideson; L. K. Forbes; S. Crozier
- **Venue / pages:** Concepts in Magnetic Resonance, 14(1), 9–18
- **Publication time:** 2002
- **DOI:** `10.1002/cmr.10000`
- **Links:** [DOI resolver](https://doi.org/10.1002/cmr.10000)
- **Abstract (EN, paraphrased):** This paper combines stream functions with the target-field method to derive complicated shim-coil winding patterns. It is aimed at cases where desired field shapes and finite geometry make traditional simple harmonic windings inadequate. The stream-function representation provides a direct route from optimized surface current density to manufacturable contours.
- **アブストラクト（日本語要約）:** stream function とターゲットフィールド法を組み合わせ、複雑なシムコイル巻線パターンを求める方法です。目標磁場形状や有限形状のために単純な調和巻線では不十分な場合を想定しています。最適化された表面電流密度から製作可能な等高線巻線へ直接変換できます。

### S08. A novel target-field method for magnetic resonance shim coils: III. Shielded zonal and tesseral coils

- **Area:** Shim
- **Authors:** L. K. Forbes; S. Crozier
- **Venue / pages:** Journal of Physics D: Applied Physics, 36(2), 68–80
- **Publication time:** 2003 Jan
- **DOI:** `10.1088/0022-3727/36/2/302`
- **Links:** [DOI resolver](https://doi.org/10.1088/0022-3727/36/2/302)
- **Abstract (EN, paraphrased):** The third paper in the series adds active shielding to finite-length zonal and tesseral shim-coil design. Primary and shield winding patterns are designed so the desired target field is generated inside the target region while the field outside the shield is suppressed. The approach extends the finite-length target-field method to shielded shim hardware.
- **アブストラクト（日本語要約）:** 有限長 zonal/tesseral シムコイル設計に能動遮蔽を加えたシリーズ第 3 論文です。一次巻線とシールド巻線を同時に設計し、内部ターゲット領域では目標場を作り、シールド外側では磁場を抑制します。有限長ターゲットフィールド法をシールド付きシムハードウェアへ拡張しています。

### S09. Shim design using a linear programming algorithm

- **Area:** Shim
- **Authors:** S. E. Ungersma et al.
- **Venue / pages:** Magnetic Resonance in Medicine, 52(3), 619–627
- **Publication time:** 2004 Sep
- **DOI:** `10.1002/mrm.20176`
- **Links:** [DOI resolver](https://doi.org/10.1002/mrm.20176); [PubMed](https://pubmed.ncbi.nlm.nih.gov/15334583/)
- **Abstract (EN, paraphrased):** A linear-programming algorithm is introduced for designing resistive shim coils on arbitrary surfaces. The method can target shim fields of any order over an arbitrary ROI and tends to produce sparse, constructible current patterns. Examples include specialized knee and head-imaging magnet geometries.
- **アブストラクト（日本語要約）:** 任意面上の抵抗性シムコイルを線形計画法で設計する手法です。任意 ROI 上で任意次数のシム場を目標にでき、構成しやすい疎な電流パターンを得やすい点が特徴です。膝用磁石や頭部用磁石など、特殊形状の設計例を扱っています。

### S10. Mitigation of susceptibility-induced signal loss in neuroimaging using localized shim coils

- **Area:** Shim
- **Authors:** J. J. Hsu; G. H. Glover
- **Venue / pages:** Magnetic Resonance in Medicine, 53(2), 243–248
- **Publication time:** 2005 Feb
- **DOI:** `10.1002/mrm.20365`
- **Links:** [DOI resolver](https://doi.org/10.1002/mrm.20365); [PubMed](https://pubmed.ncbi.nlm.nih.gov/15678595/)
- **Abstract (EN, paraphrased):** The paper demonstrates localized resistive shim coils for reducing susceptibility-induced B0 inhomogeneity in neuroimaging. Coils placed close to problematic anatomy are optimized in situ for patient-specific correction. The approach improves field homogeneity and recovers signal in regions that are difficult for global spherical-harmonic shims.
- **アブストラクト（日本語要約）:** 神経画像で感受率由来の B0 不均一による信号低下を低減するため、局所抵抗シムコイルを用います。問題部位に近い位置へコイルを置き、被験者ごとの in situ 最適化を行います。全体的な球面調和シムでは補正しにくい領域の均一性改善と信号回復を狙います。

### S11. Quantitative Comparison of Minimum Inductance and Minimum Power Algorithms for the Design of Shim Coils for Small Animal Imaging

- **Area:** Shim
- **Authors:** P. Hudson; S. D. Hudson; W. B. Handler; T. J. Scholl; B. A. Chronik
- **Venue / pages:** Concepts in Magnetic Resonance Part B, 37B(2), 65–74
- **Publication time:** 2010 Apr
- **DOI:** `10.1002/cmr.b.20159`
- **Links:** [DOI resolver](https://doi.org/10.1002/cmr.b.20159); [PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC2857351/)
- **Abstract (EN, paraphrased):** This paper compares minimum-inductance and minimum-power target-field algorithms for high-order shim sets designed for small-animal imaging. The authors evaluate inductive and resistive merits for multiple shim axes and compare continuous and discretized winding patterns. Minimum-power designs reduce dissipation, while minimum-inductance designs favor switching speed; the observed performance differences are generally modest.
- **アブストラクト（日本語要約）:** 小動物イメージング用の高次シムセットについて、最小インダクタンス法と最小電力法を定量比較しています。複数シム軸でインダクタンス指標と抵抗指標を評価し、連続解と離散巻線も比較します。最小電力設計は発熱・消費電力を下げ、最小インダクタンス設計は高速切替に有利ですが、性能差は比較的小さいとされています。

### S12. Magnetic Field Homogenization of the Human Prefrontal Cortex with a Set of Localized Electrical Coils

- **Area:** Shim
- **Authors:** C. Juchem et al.
- **Venue / pages:** Magnetic Resonance in Medicine, 63(1), 171–180
- **Publication time:** 2010 Jan
- **DOI:** `10.1002/mrm.22164`
- **Links:** [DOI resolver](https://doi.org/10.1002/mrm.22164); [PubMed](https://pubmed.ncbi.nlm.nih.gov/19918903/)
- **Abstract (EN, paraphrased):** The authors use localized electrical coils to homogenize the human prefrontal cortex, where susceptibility gradients are strong. The local coils generate high-amplitude correction fields close to the target while minimizing undesired effects elsewhere. Combined with low-order spherical-harmonic shimming, the approach reduces signal dropout in high-field gradient-echo imaging.
- **アブストラクト（日本語要約）:** 感受率勾配の強いヒト前頭前野を均一化するため、局所電気コイルを用いる研究です。局所コイルはターゲット近傍で大きな補正場を生成し、他領域への影響を小さく保ちます。低次球面調和シムと組み合わせることで、高磁場 gradient-echo 画像の信号欠落を低減します。

### S13. Magnetic field modeling with a set of individual localized coils

- **Area:** Shim / Encoding
- **Authors:** C. Juchem; T. W. Nixon; A. C. McIntyre; R. A. de Graaf
- **Venue / pages:** Journal of Magnetic Resonance, 204(2), 281–289
- **Publication time:** 2010 Jun
- **DOI:** `10.1016/j.jmr.2010.03.008`
- **Links:** [DOI resolver](https://doi.org/10.1016/j.jmr.2010.03.008); [PubMed](https://pubmed.ncbi.nlm.nih.gov/20347360/)
- **Abstract (EN, paraphrased):** This paper models magnetic fields generated by many independent localized coils. The same basis of individual coil fields can synthesize shim fields and, in some cases, spatial-encoding gradients. The study anticipates multi-coil field control, where the effective volume and correction field can be adapted by optimizing currents rather than by relying only on fixed spherical-harmonic hardware.
- **アブストラクト（日本語要約）:** 多数の独立した局所コイルが生成する磁場をモデル化しています。個別コイル場の基底を使って、シム場だけでなく場合によっては空間エンコード勾配も合成できます。固定的な球面調和ハードウェアだけでなく、電流最適化により有効体積や補正場を変えられる multi-coil field control の基礎となる研究です。

### S14. Multicoil shimming of the mouse brain

- **Area:** Shim
- **Authors:** C. Juchem et al.
- **Venue / pages:** Magnetic Resonance in Medicine, 66(3), 893–900
- **Publication time:** 2011 Sep
- **DOI:** `10.1002/mrm.22850`
- **Links:** [DOI resolver](https://doi.org/10.1002/mrm.22850); [PubMed](https://pubmed.ncbi.nlm.nih.gov/21394781/)
- **Abstract (EN, paraphrased):** A 48-coil local shim array is used for static and dynamic shimming of the mouse brain at high field. The multi-coil basis reduces residual B0 distortions more effectively than conventional second-order spherical-harmonic shimming. The paper demonstrates improved gradient-echo signal recovery and localized correction flexibility.
- **アブストラクト（日本語要約）:** 高磁場でマウス脳の静的・動的シミングを行うため、48 個の局所コイルアレイを用います。multi-coil 基底は従来の 2 次球面調和シムより残留 B0 歪みを低減します。gradient-echo 信号の回復と、局所補正の柔軟性を示しています。

### S15. Dynamic multi-coil shimming of the human brain at 7 T

- **Area:** Shim
- **Authors:** C. Juchem et al.
- **Venue / pages:** Journal of Magnetic Resonance, 212(2), 280–288
- **Publication time:** 2011 Oct
- **DOI:** `10.1016/j.jmr.2011.07.005`
- **Links:** [DOI resolver](https://doi.org/10.1016/j.jmr.2011.07.005); [PubMed](https://pubmed.ncbi.nlm.nih.gov/21840753/)
- **Abstract (EN, paraphrased):** The authors demonstrate dynamic slice-specific shimming of the human brain at 7 T using an array of 48 localized coils. Non-orthogonal coil basis fields are optimized for each slice, reducing B0 inhomogeneity beyond what is possible with dynamic low-order spherical-harmonic shims. The paper is central for multi-coil B0 control at ultra-high field.
- **アブストラクト（日本語要約）:** 7 T ヒト脳で、48 個の局所コイルアレイによるスライスごとの動的シミングを示しています。非直交のコイル基底場を各スライスで最適化し、低次球面調和シムの動的補正を超える B0 均一化を実現します。超高磁場における multi-coil B0 制御の中心的文献です。

### S16. A novel approach to designing cylindrical-surface shim coils for a superconducting magnet of magnetic resonance imaging

- **Area:** Shim
- **Authors:** W.-T. Liu; D.-L. Zu; X. Tang
- **Venue / pages:** Chinese Physics B, 19(1), 018701
- **Publication time:** 2010 Jan
- **DOI:** `10.1088/1674-1056/19/1/018701`
- **Links:** [DOI resolver](https://doi.org/10.1088/1674-1056/19/1/018701); [Chinese Physics B](https://cpb.iphy.ac.cn/EN/10.1088/1674-1056/19/1/018701)
- **Abstract (EN, paraphrased):** This paper designs finite-length cylindrical gradient and shim coils by relating harmonic terms in cylindrical current distributions to spherical-harmonic field components. The method uses matrix inversion and stream functions to obtain discrete wire distributions without specifying target-field points. It is intended for pure-harmonic shim fields in superconducting MRI magnets.
- **アブストラクト（日本語要約）:** 円筒面上の電流分布の調和成分と、磁場の球面調和成分を関係づけ、有限長の円筒勾配・シムコイルを設計します。ターゲットフィールド点を設定せず、行列反転と stream function から離散巻線分布を得ます。超電導 MRI 磁石の純調和シム場生成を目的とした方法です。

### S17. A novel target-field approach to design bi-planar shim coils for permanent-magnet MRI

- **Area:** Shim
- **Authors:** W. Liu; X. Tang; D. Zu
- **Venue / pages:** Concepts in Magnetic Resonance Part B, 37B(1), 29–38
- **Publication time:** 2010 Feb
- **DOI:** `10.1002/cmr.b.20153`
- **Links:** [DOI resolver](https://doi.org/10.1002/cmr.b.20153); [Ovid record](https://www.ovid.com/journals/cimrb/fulltext/10.1002/cmr.b.20153~a-novel-targetfield-approach-to-design-biplanar-shim-coils)
- **Abstract (EN, paraphrased):** The paper adapts target-field design to biplanar shim coils for permanent-magnet MRI. It focuses on the open, planar geometry often used in permanent magnets and derives winding patterns that generate desired shim fields over the imaging region. The method is relevant to compact low-field systems where conventional cylindrical shims are unsuitable.
- **アブストラクト（日本語要約）:** 永久磁石 MRI 用のバイプラナ・シムコイルにターゲットフィールド設計を適用した論文です。永久磁石でよく用いられる開放的な平面形状を対象とし、撮像領域に必要なシム場を作る巻線パターンを導出します。従来の円筒シムが適さないコンパクト低磁場系に関係します。

### S18. Theory and development of biplanar active shim coils for a permanent NMR analyzer

- **Area:** Shim
- **Authors:** T. Xia; Z. Miao; S. Chen; H. Wang; Y. Yao
- **Venue / pages:** PLOS ONE, 12(7), e0181552
- **Publication time:** 2017 Jul
- **DOI:** `10.1371/journal.pone.0181552`
- **Links:** [DOI resolver](https://doi.org/10.1371/journal.pone.0181552); [PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0181552); [PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC5524427/)
- **Abstract (EN, paraphrased):** The authors derive biplanar active shim-coil fields from scalar and vector potential formulations and include sine and cosine harmonic components. They design and fabricate nine biplanar shim coils for a permanent NMR analyzer. Experimental shimming demonstrates that the developed harmonic-field design procedure is practical.
- **アブストラクト（日本語要約）:** スカラー・ベクトルポテンシャルからバイプラナ能動シムコイルの磁場式を導き、sin/cos 調和成分を含めて扱います。永久磁石 NMR アナライザ用に 9 個のバイプラナシムコイルを設計・製作しています。実験的シミングにより、調和場に基づく設計手順の実用性を示しています。

### S19. Design of biplanar shim coils for ultra-low field MRI

- **Area:** Shim
- **Authors:** Y. He; W. He; B. Xiong; P. Guo; Z. Xu
- **Venue / pages:** International Journal of Applied Electromagnetics and Mechanics, 58(3)
- **Publication time:** 2018 Nov
- **DOI:** `10.3233/JAE-180025`
- **Links:** [DOI resolver](https://doi.org/10.3233/JAE-180025); [SAGE page](https://journals.sagepub.com/doi/full/10.3233/JAE-180025)
- **Abstract (EN, paraphrased):** This paper designs first- and second-order biplanar active shim coils for a 50 mT ultra-low-field MRI system. The measured main field is expanded in orthogonal spherical harmonics, and harmonic coefficients guide the required shim terms. The work is directly relevant to low-field systems where magnet homogeneity strongly affects signal-to-noise ratio.
- **アブストラクト（日本語要約）:** 50 mT の超低磁場 MRI 用に、1 次および 2 次のバイプラナ能動シムコイルを設計します。測定された主磁場を直交球面調和関数で展開し、その係数から必要なシム項を決めます。磁場均一性が SNR に直結する低磁場 MRI に直接関係する論文です。

### S20. Design of a shim coil array matched to the human brain anatomy

- **Area:** Shim
- **Authors:** F. Jia et al.
- **Venue / pages:** Magnetic Resonance in Medicine, 83(4), 1442–1457
- **Publication time:** 2020 Apr
- **DOI:** `10.1002/mrm.28016`
- **Links:** [DOI resolver](https://doi.org/10.1002/mrm.28016); [PubMed](https://pubmed.ncbi.nlm.nih.gov/31559670/)
- **Abstract (EN, paraphrased):** The authors design multi-channel shim coil arrays whose geometry is matched to human brain anatomy and measured B0 field-map statistics. Stream-function methods and singular-value decomposition are used with cross-validation over many subjects and head positions. The resulting arrays outperform high-order spherical-harmonic shims with fewer, anatomically optimized elements.
- **アブストラクト（日本語要約）:** ヒト脳の形状と実測 B0 field map の統計に合わせた多チャネルシムコイルアレイを設計しています。stream function 法と特異値分解を用い、多数被験者・頭位で交差検証します。解剖学的に最適化された少数要素で、高次球面調和シムを上回る性能を示します。

### S21. The orthogonal shim coil for 3-Tesla brain imaging

- **Area:** Shim
- **Authors:** Y. Zhou et al.
- **Venue / pages:** Magnetic Resonance in Medicine, 83(4), 1499–1511
- **Publication time:** 2020 Apr
- **DOI:** `10.1002/mrm.28010`
- **Links:** [DOI resolver](https://doi.org/10.1002/mrm.28010); [PubMed](https://pubmed.ncbi.nlm.nih.gov/31631369/)
- **Abstract (EN, paraphrased):** This paper proposes an orthogonal shim-coil array for 3 T brain imaging, with coil planes arranged to reduce interaction with neighboring RF coils. Simulation and experiment show improved B0 homogeneity while limiting RF-performance penalties. It is an example of shim-array design under simultaneous electromagnetic and receive-array constraints.
- **アブストラクト（日本語要約）:** 3 T 脳 MRI 用に、隣接 RF コイルとの干渉を抑える直交配置のシムコイルアレイを提案しています。シミュレーションと実験により、RF 性能低下を抑えながら B0 均一性を改善できることを示します。シムアレイ設計を RF 受信アレイ制約と同時に考える例です。

### S22. A fieldmap-driven few-channel shim coil design for MRI of the human brain

- **Area:** Shim
- **Authors:** L. Pinho Meneses; A. Amadon
- **Venue / pages:** Physics in Medicine & Biology, 66(1), 015001
- **Publication time:** 2021 Jan
- **DOI:** `10.1088/1361-6560/abc810`
- **Links:** [DOI resolver](https://doi.org/10.1088/1361-6560/abc810); [IOPscience](https://iopscience.iop.org/article/10.1088/1361-6560/abc810)
- **Abstract (EN, paraphrased):** This paper designs a small number of shim coils from measured human-brain B0 field maps. Subject-specific stream functions are computed under low-power constraints, and principal component analysis extracts dominant correction modes. The resulting few-channel coils can outperform many conventional spherical-harmonic channels in difficult regions such as the prefrontal cortex.
- **アブストラクト（日本語要約）:** ヒト脳の実測 B0 field map から、少数チャネルのシムコイルを設計します。低電力制約下で被験者ごとの stream function を求め、主成分分析で支配的な補正モードを抽出します。前頭前野など難しい領域では、多数の従来球面調和チャネルを上回る可能性があります。

### S23. Systematic dimensional analysis of the scaling relationship for gradient and shim coil design parameters

- **Area:** Gradient / Shim
- **Authors:** S.-K. Lee; M. A. Bernstein
- **Venue / pages:** Magnetic Resonance in Medicine, 88(4), 1901–1911
- **Publication time:** 2022 Oct
- **DOI:** `10.1002/mrm.29316`
- **Links:** [DOI resolver](https://doi.org/10.1002/mrm.29316); [PubMed](https://pubmed.ncbi.nlm.nih.gov/35666832/); [PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC9893842/)
- **Abstract (EN, paraphrased):** The paper derives scaling relationships for gradient and shim coil design parameters using dimensional analysis. For gradients and higher-order shims, it relates inductance, efficiency, and characteristic coil dimension, extending the design figure-of-merit concept to l-th order shim fields. It is useful when comparing coils across different scales and harmonic orders.
- **アブストラクト（日本語要約）:** 次元解析により、勾配コイルおよびシムコイルの設計パラメータのスケーリング関係を導きます。勾配および高次シムについて、インダクタンス、効率、代表寸法の関係を整理し、l 次シム場に対する figure-of-merit を拡張しています。異なるサイズや調和次数のコイル比較に有用です。

### S24. Improving brain B0 shimming using an easy and accessible multi-coil shim array at ultra-high field

- **Area:** Shim
- **Authors:** A. Boër et al.
- **Venue / pages:** MAGMA, 35, 943–951
- **Publication time:** 2022
- **DOI:** `10.1007/s10334-022-01014-6`
- **Links:** [DOI resolver](https://doi.org/10.1007/s10334-022-01014-6); [Springer](https://link.springer.com/article/10.1007/s10334-022-01014-6)
- **Abstract (EN, paraphrased):** The paper presents a relatively simple multi-coil shim array for ultra-high-field brain MRI. The design aims at accessibility and practical construction rather than maximum channel count. Static and slice-based shimming tests show measurable improvements over conventional second-order shimming.
- **アブストラクト（日本語要約）:** 超高磁場脳 MRI 用に、比較的簡単で構成しやすい multi-coil シムアレイを提案しています。最大チャネル数よりも、アクセス性と製作容易性を重視した設計です。静的シムおよびスライス単位シムで、従来の 2 次シムに対する改善を示しています。

### S25. Design and realization of a multi-coil array for B0 field control in a compact 1.5T head-only MRI scanner

- **Area:** Shim / Encoding
- **Authors:** J. Theilenberg et al.
- **Venue / pages:** Magnetic Resonance in Medicine, 90(3), 1228–1241
- **Publication time:** 2023 Sep
- **DOI:** `10.1002/mrm.29692`
- **Links:** [DOI resolver](https://doi.org/10.1002/mrm.29692); [PubMed](https://pubmed.ncbi.nlm.nih.gov/37078562/)
- **Abstract (EN, paraphrased):** This work designs and realizes a 31-channel multi-coil array for B0 field generation, image encoding, and advanced shimming in a compact 1.5 T head-only scanner. The design is evaluated in simulation and bench tests, including gradient strength, cooling, and duty-cycle considerations. It demonstrates how multi-coil hardware can blur the line between shimming and encoding.
- **アブストラクト（日本語要約）:** コンパクトな 1.5 T 頭部専用 MRI に対し、B0 場生成、画像エンコード、高度シミングを担う 31 チャネル multi-coil アレイを設計・実装しています。シミュレーションとベンチ試験で、勾配強度、冷却、デューティ比を評価しています。multi-coil ハードウェアがシムとエンコードの境界を曖昧にできることを示します。

### S26. Passive shimming method for permanent magnet MRI based on dynamic target magnetic field

- **Area:** Shim
- **Authors:** Xin Liu; Jianli Meng; Chuangxin Huang; Qi Chen
- **Venue / pages:** Physics Open, article 100296
- **Publication time:** 2025
- **DOI:** `10.1016/j.physo.2025.100296`
- **Links:** [DOI resolver](https://doi.org/10.1016/j.physo.2025.100296); [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2666032625000468)
- **Abstract (EN, paraphrased):** This paper proposes a passive-shimming optimization method for permanent-magnet MRI based on a dynamic target magnetic field. Instead of fixing all target values rigidly, the approach updates target field values to enlarge the feasible solution space. An optimization model and revised simplex-style solution are used to place correction pieces more effectively.
- **アブストラクト（日本語要約）:** 永久磁石 MRI 向けに、動的ターゲット磁場に基づく受動シミング最適化を提案しています。ターゲット磁場値を固定しすぎず、動的に更新することで実行可能解空間を広げます。最適化モデルと改良 simplex 系の解法により、補正片配置を効率化する設計です。

### S27. Passive shimming performance in 3 T MRI systems: Influence of shim parameters under varying magnet field distributions

- **Area:** Shim
- **Authors:** Jinhao Liu; Miutian Wang; Wenchen Wang; Yaohui Wang; Wenhui Yang; Weimin Wang; Feng Liu
- **Venue / pages:** Journal of Magnetic Resonance, 381, 107969
- **Publication time:** 2025 Dec
- **DOI:** `10.1016/j.jmr.2025.107969`
- **Links:** [DOI resolver](https://doi.org/10.1016/j.jmr.2025.107969); [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1090780725001417)
- **Abstract (EN, paraphrased):** This paper analyzes passive-shimming performance for 3 T MRI systems under different initial magnet field distributions. It combines optimization and sampling of shim parameters to study how slot configuration and correction-piece design affect residual harmonics. The result is relevant when passive shimming must be robust across magnet-field error patterns.
- **アブストラクト（日本語要約）:** 3 T MRI における受動シミング性能を、異なる初期磁場分布の下で解析しています。シムパラメータの最適化とサンプリングを組み合わせ、スロット構成や補正片設計が残留調和成分に与える影響を調べます。磁石誤差パターンに対して頑健な受動シミングを検討する際に有用です。

## Notes for use

- The boundary between gradient coils and first-order shim coils is partly conventional: both generate controlled spatial variations in B0, but gradient coils are normally designed for rapid switching and encoding, whereas shim coils are designed for field homogenization or slow/dynamic B0 correction.
- For formal citation, verify author spellings, issue numbers, and article-number metadata in the linked publisher or PubMed record. A few recent entries use article numbers rather than page ranges.
- If the goal is low-field or permanent-magnet MRI, the most directly relevant entries are G30, G34, G35, S17, S18, S19, and S26, plus the general methods G19, G23, G25, and S23.
