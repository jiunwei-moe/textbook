PANDOC_OPTS := --smart -N --filter ../scripts/filter.py --no-highlight

ch_dirs := $(wildcard ch*)
dist_md := $(ch_dirs:%=dist/%.md)
dist_html := $(ch_dirs:%=dist/%.html)
dist_docx := $(ch_dirs:%=dist/%.docx)
dist_icml := $(ch_dirs:%=dist/%.icml)
diagrams_pdf := $(wildcard $(ch_dirs:%=%/diagrams/*.pdf))
diagrams_png := $(diagrams_pdf:%.pdf=%.png)

all: $(diagrams_png) $(dist_html) $(dist_docx) $(dist_icml)

dist/%.md: %/*.md
	mkdir -p $(dir $@)
	. ~/.virtualenvs/textbook/bin/activate && \
	python scripts/preprocessor.py $< > $@
	mkdir -p $(dir $@)diagrams
	cp $(dir $<)diagrams/*.pdf $(dir $@)diagrams 

%.png: %.pdf
	mogrify -format png $^

%.html: %.md pandoc.css
	. ~/.virtualenvs/textbook/bin/activate && \
	cd $(basename $(notdir $@)) && \
	pandoc -s -o ../$@ -c ../pandoc.css --self-contained --number-offset=$(subst ch,,$(basename $(notdir $@))) $(PANDOC_OPTS) ../$<

%.docx: %.md reference.docx
	. ~/.virtualenvs/textbook/bin/activate && \
	cd $(basename $(notdir $@)) && \
	pandoc -s -o ../$@ --reference-docx=../reference.docx --number-offset=$(subst ch,,$(basename $(notdir $@))) $(PANDOC_OPTS) ../$<

%.icml: %.md
	. ~/.virtualenvs/textbook/bin/activate && \
	cd $(basename $(notdir $@)) && \
	pandoc -s -o ../$@ --number-offset=$(subst ch,,$(basename $(notdir $@))) $(PANDOC_OPTS) ../$<

clean:
	rm -rf dist
