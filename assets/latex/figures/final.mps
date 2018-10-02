verbatimtex
%&latex 
\documentclass{article} 
\usepackage{avm}
\begin{document}
etex

input boxes;
input trees;

beginfig(1);

  tree.a1(btex $S$ etex)
         (leaf(btex $NP$ etex),
          tree.a2(btex $VP$ etex)
                  (leaf.a5(btex \textit{Verb} etex)));
         
  a1.c = (0,0);
  drawtrees(a1);

  label.rt(btex \small\begin{avm} \[ subcat: \@5 \[ first: \[ \] \\ rest: end \] \] \end{avm} etex, a2.e);
  label.lft(btex \small\begin{avm} \[ subcat: \@5 \] \end{avm} etex, a5.w);

endfig;

beginfig(2);

  tree.a1(btex $S$ etex)
         (leaf(btex $NP$ etex),
          tree.a2(btex $VP$ etex)
              (tree.a3(btex $VP$ etex)
                      (leaf.a5(btex \textit{Verb} etex)),
               leaf.a7(btex $X$ etex)));
         
  a1.c = (0,0);
  drawtrees(a1);

  label.rt(btex \small\begin{avm} \[ subcat: \@5 \[ first: \[ \] \\ rest: end \] \] \end{avm} etex, a2.e);
  label.lft(btex \small\begin{avm} \[ subcat: \@2 \[ first: \@3 \\ rest: \@5 \] \] \end{avm} etex, a3.w);
  label.rt(btex \small\begin{avm} \[ cat: \@3 NP \] \end{avm} etex, a7.e);
  label.lft(btex \small\begin{avm} \[ subcat: \@2 \] \end{avm} etex, a5.w);

endfig;

beginfig(3);

  tree.a1(btex $S$ etex)
         (leaf(btex $NP$ etex),
          tree.a2(btex $VP$ etex)
              (tree.a3(btex $VP$ etex)
                   (tree.a4(btex $VP$ etex)
                        (leaf.a5(btex \textit{Verb} etex)),
                    leaf.a6(btex $X$ etex)),
               leaf.a7(btex $X$ etex)));
         
  a1.c = (0,0);
  drawtrees(a1);

  label.rt(btex \small\begin{avm} \[ subcat: \@5 \[ first: \[ \] \\ rest: end \] \] \end{avm} etex, a2.e);
  label.lft(btex \small\begin{avm} \[ subcat: \@2 \[ first: \@3 \\ rest: \@5 \] \] \end{avm} etex, a3.w);
  label.rt(btex \small\begin{avm} \[ cat: \@3 NP \] \end{avm} etex, a7.e);
  label.lft(btex \small\begin{avm} \[ subcat: \@4 \[ first: \@1 \\ rest: \@2 \] \] \end{avm} etex, a4.w);
  label.rt(btex \small\begin{avm} \[ cat: \@1 NP \] \end{avm} etex, a6.e);
  label.lft(btex \small\begin{avm} \[ subcat: \@4 \] \end{avm} etex, a5.w);

endfig;

end;

%verbatimtex
%\end{document}
%etex

