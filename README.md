# This repo is the home of GNN part in LISA.

## This repo has the following directories.
- data: store generated DFGs, dumped DFGs for a particular framework, generated labels, and training dataset. 
- dfg_generatror: generate DFGs, and dump DFGs for a particular framework. All the generated data is stored in ***data*** folder.
- lisa_gnn_model: all the GNN models.

## Instrcutions to use LISA (currently, the default framework is CGRA_ME. Will add a parameter later).
For the following examples, we use *platform* to represent compiler framework name such as *cgra_me*, and use *arch_name* to represent architecture name such as cgra_me_4_4 that means a 4x4 CGRA.

- First, activate lisa environment.
  > conda activate lisa 

- generate traninng graph (in *dfg_generator*)
  > python dfg_generator.py -s 0 - n 10 -d platform

  -s: the start index of graph. Optional, the deafult value is 0 <br>
  -n: the number of generated graphed. Optional, the default value is 10 <br>
  This generates a folder *platform* under "*data*", and generate two folders *platform* and *graph* under "*data/platform/*". <br>
  data/platform/graph: contain the standarded graph. <br>
  data/platform/platform: contain the converted graph from the standarded graph to let the compiler to take as input DFG. 


- transform graph (in *dfg_generator*)
  > python dfg_transformer.py -s graph -d transformered_graph --home_directory platform

  --home_directory: the home directory of other directories. This folder is under "*data*"
  -s: the source dir of graphes. Optional, the deafult value is "graph" <br>
  -d: the destination dir of transformed graphes. Optional, the default value is "transformered_graph" <br>
 

- label fiter and generate training dataset (in *data*)
  >python label_filter.py -r transformered_graph -l arch_name

  -r: raw graph, i.e, the directory of transformed graph (data/platform/transformered_graph)<br>
  -l: the directory of labels (data/labels/arch_name). <br>
  This command will generate a folder in training_dataset. The folder name is the same as *label_dir**. This folder has the training dataset

- run training (in *lisa_gnn_model*)
  > bash run_training.sh arch_name
  
  This will train all the models for this arch and save all the model with name "*arch_name*"

- run inference (in *lisa_gnn_model*)
  > python gnn_inference.py graph_name arch_name
  
  The graph name is a file in "*dara/infer/*". For example, for a graph file "3c4c.txt", the input should be 3c4c.





## Some useful commands in git:
- check whether the submodule has been pushed before pushing the main project 
 > git push --recurse-submodules=check