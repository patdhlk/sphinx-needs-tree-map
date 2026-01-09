# Makefile for Task Management System Documentation
#
# This example demonstrates the sphinx-needs-tree-map extension

SPHINXOPTS    ?=
SPHINXBUILD   ?= uv run sphinx-build
SOURCEDIR     = docs
BUILDDIR      = _build

.PHONY: help clean html livehtml

help:
	@echo "Available targets:"
	@echo "  html      - Build HTML documentation"
	@echo "  clean     - Remove build directory"
	@echo "  livehtml  - Build and serve with live reload (requires sphinx-autobuild)"

clean:
	rm -rf $(BUILDDIR)

html:
	$(SPHINXBUILD) -b html $(SOURCEDIR) $(BUILDDIR)/html $(SPHINXOPTS)
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."
	@echo "Open $(BUILDDIR)/html/index.html in your browser to view."

livehtml:
	uv run sphinx-autobuild $(SOURCEDIR) $(BUILDDIR)/html $(SPHINXOPTS)
