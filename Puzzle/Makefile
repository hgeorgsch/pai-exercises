
eqAstar.log: Astar.py

%.log: %.py
	python3 $< >&1 | tee $@

clean:
	rm -f *.log
